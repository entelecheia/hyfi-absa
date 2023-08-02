import datetime
import json

from hyfi.composer import BaseModel

from hyabsa import HyFI
from hyabsa.llms import ChatCompletionResponse

logger = HyFI.getLogger(__name__)


class AgentResult(BaseModel):
    timestamp: str = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
    parsed: str
    usage: dict
    response: dict

    @classmethod
    def from_chat_reponse(
        cls,
        response: ChatCompletionResponse,
    ) -> "AgentResult":
        try:
            response = json.loads(response.content)
            result = cls(
                parsed="success",
                usage=response.usage,
                response=response,
            )
        except json.decoder.JSONDecodeError:
            result = cls(
                parsed="failed",
                usage=response.usage,
                response=response,
            )
        return result