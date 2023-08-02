from typing import List, Optional, Union

from datasets import Dataset
from hyfi.run import RunConfig
from hyfi.runner import BaseRunner

from hyabsa import HyFI
from hyabsa.agents import AbsaAgent

logger = HyFI.getLogger(__name__)


class AbsaRunner(BaseRunner):
    _config_name_: str = "absa"
    _auto_populate_: bool = True

    agent: AbsaAgent = AbsaAgent()
    tasks: Optional[List[str]] = []
    data_load: RunConfig = RunConfig(_config_name_="load_dataset")
    data_save: RunConfig = RunConfig(_config_name_="save_dataset_to_disk")

    text_col: str = "bodyText"
    batch_size: int = 1000
    num_workers: int = 1
    remove_columns: Optional[Union[List[str], str]] = None
    load_from_cache_file: bool = True

    _dataset: Optional[Dataset] = None

    @property
    def dataset(self) -> Dataset:
        if self._dataset is None:
            self._dataset = self.load_dataset()
        return self._dataset

    def load_dataset(self) -> Dataset:
        return HyFI.partial(self.data_load.config)()

    def save_dataset(self, dataset: Dataset) -> None:
        HyFI.partial(self.data_save.config)(dataset)

    def run(self):
        dataset = self.load_dataset()
        tasks = self.tasks or ["QUAD"]
        for task in tasks:
            logger.info("Predicting %s...", task)
            dataset = dataset.map(
                batch_run,
                batched=True,
                batch_size=self.batch_size,
                num_proc=self.num_workers,
                fn_kwargs={
                    "task": task,
                    "agent": self.agent.model_copy(),
                    "text_col": self.text_col,
                },
                remove_columns=self.remove_columns,
                load_from_cache_file=self.load_from_cache_file,
            )
        if self.verbose:
            print(dataset[0])
        self.save_dataset(dataset)


def batch_run(
    batch,
    task: str = "QUAD",
    agent: AbsaAgent = None,
    text_col: str = "bodyText",
) -> dict:
    if agent is None:
        agent = {}
    model = agent
    model.task = task
    if model.verbose:
        print(model)

    res = [execute_each(text, model) for text in batch[text_col]]
    return {f"{task}_pred": res}


def execute_each(
    text: str,
    agent: AbsaAgent,
) -> str:
    response = agent.execute(text)
    if agent.verbose:
        logger.info(
            "Task: %s | Text:\n%s\n | Response:\n%s\n",
            agent.task,
            text,
            response,
        )

    return response
