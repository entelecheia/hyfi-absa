import datetime
import json
import time
from typing import Any, Dict, Optional, Tuple

import backoff
import openai
from hyfi.composer import BaseModel
from openai.error import (
    APIConnectionError,
    APIError,
    InvalidRequestError,
    RateLimitError,
    ServiceUnavailableError,
)

from hyabsa import HyFI

logger = HyFI.getLogger(__name__)


class OpenaiAPI(BaseModel):
    _config_group_: str = "api"
    _config_name_: str = "openai"

    api_key: Optional[str] = None
    model: str = "gpt-3.5-turbo-0301"
    rate_limit_per_minute: int = 3500
    temperature: float = 0.0

    _engine_: Optional[openai.ChatCompletion] = None

    def init_api(self, api_key: Optional[str] = None):
        api_key = api_key or self.api_key
        denv = HyFI.dotenv()
        if not api_key and denv.OPENAI_API_KEY:
            api_key = denv.OPENAI_API_KEY.get_secret_value()
        if not api_key:
            raise ValueError("OpenAI API Key is required.")
        self._engine_ = openai.ChatCompletion()
        logger.info("OpenAI ChatCompletion API is initialized.")

    def predict(self, text: str, prompt: str) -> Dict[str, Any]:
        args = {
            "model": self.model_name,
            "temperature": self.temperature,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }
        delay = 60.0 / self.rate_limit_per_minute
        content, usage, _ = call_api(self._engine_, args, delay_in_seconds=delay)
        return parse_response_to_json(content, usage, text)


@backoff.on_exception(
    backoff.expo,
    (
        RateLimitError,
        APIConnectionError,
        APIError,
        ServiceUnavailableError,
    ),
)
def request_api(engine, args, delay_in_seconds: float = 1):
    time.sleep(delay_in_seconds)
    return engine.create(**args)


def call_api(engine, args, delay_in_seconds: float = 1) -> Tuple[str, dict, Any]:
    time.sleep(delay_in_seconds)
    try:
        response = request_api(engine, args, delay_in_seconds=delay_in_seconds)
        message = response["choices"][0]["message"]
        content = message["content"].strip().strip("\n")
        usage = response["usage"]
        return content, usage, response
    except InvalidRequestError as e:
        logger.error(e)
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        return str(e.user_message), usage, e
    except Exception as e:
        logger.error(e)
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        return str(e), usage, e


def parse_response_to_json(
    response: str,
    usage: dict,
    text: str,
) -> Dict[str, Any]:
    try:
        response = json.loads(response)
        result = {
            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
            "parsed": "success",
            "usage": usage,
            "response": response,
            "text": text,
        }
    except json.decoder.JSONDecodeError:
        result = {
            "timestamp": f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
            "parsed": "failed",
            "usage": usage,
            "response": response,
            "text": text,
        }
    return result
