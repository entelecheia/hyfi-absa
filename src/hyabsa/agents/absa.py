import json

from hyabsa import HyFI
from hyabsa.llms import OpenAIChatCompletion

from .base import BaseAgent
from .results import AgentResult

logger = HyFI.getLogger(__name__)


class AbsaAgent(BaseAgent):
    _config_name_: str = "absa"
    llm: OpenAIChatCompletion = OpenAIChatCompletion()

    def execute(self, text: str) -> str:
        result = AgentResult.from_chat_reponse(
            self.llm.request(self.build_message(text))
        )
        if self.output_filepath:
            HyFI.append_to_jsonl(result.model_dump(), self.output_filepath)
        return json.dumps(result.model_dump(), ensure_ascii=False)
