import json
from typing import Optional

from hyfi.composer import BaseModel

from hyabsa import HyFI
from hyabsa.api import OpenaiAPI
from hyabsa.prompts import Prompts

logger = HyFI.getLogger(__name__)


class AbsaAgent(BaseModel):
    api: OpenaiAPI = OpenaiAPI()
    prompts: Prompts = Prompts()
    absa_task: str = "AE"
    prompt_name: str = "base"
    output_dir: str = "outputs/preds"
    save_filename: Optional[str] = None
    verbose: bool = False

    @property
    def model_name(self) -> str:
        return self.api.model.replace(".", "")

    @property
    def save_filepath(self) -> str:
        save_filename = (
            self.save_filename
            or f"{self.absa_task}_{self.prompt_name}_{self.model_name}.jsonl"
        )
        return f"{self.output_dir}/{save_filename}"

    def generate_prompt(self, text: str) -> str:
        task = self.absa_task
        prompt = self.prompts.get_prompt(task, self.prompt_name)
        prompt += f'\nInput text:\n"{text}"\nAnswer:\n'
        return prompt

    def predict(self, text: str) -> str:
        result = self.api.predict(text, self.generate_prompt(text))
        if self.save_filepath:
            HyFI.append_to_jsonl(result, self.save_filepath)
        # remove text from result to save space
        del result["text"]
        return json.dumps(result, ensure_ascii=False)
