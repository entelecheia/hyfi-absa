from typing import List, Optional, Union

from datasets import Dataset
from hyabsa.agents import AbsaAgent

from hyabsa import HyFI  # type: ignore

logger = HyFI.getLogger(__name__)


def predict_each(
    text: str,
    agent: AbsaAgent,
) -> str:
    response = agent.predict(text)
    if agent.verbose:
        logger.info(
            "Task: %s | Text:\n%s\n | Response:\n%s\n",
            agent.absa_task,
            text,
            response,
        )

    return response


def batch_predict(
    batch,
    task: str = "QUAD",
    agent_name: str = "openai",
    text_col: str = "bodyText",
) -> dict:
    cfg = HyFI.compose_as_dict(f"agent={agent_name}")
    model = AbsaAgent(**cfg)
    model.absa_task = task
    model.init_api()
    if model.verbose:
        print(model)

    res = [predict_each(text, model) for text in batch[text_col]]
    return {f"{task}_pred": res}


def absa_agent_predict(
    dataset: Dataset,
    tasks: Optional[List[str]] = None,
    agent_name: str = "openai",
    text_col: str = "bodyText",
    batch_size: int = 1000,
    num_workers: int = 1,
    remove_columns: Optional[Union[List[str], str]] = None,
    load_from_cache_file=True,
    verbose=False,
) -> Dataset:
    if tasks is None:
        tasks = ["QUAD"]
    for task in tasks:
        logger.info("Predicting %s...", task)
        dataset = dataset.map(
            batch_predict,
            batched=True,
            batch_size=batch_size,
            num_proc=num_workers,
            fn_kwargs={
                "task": task,
                "agent_name": agent_name,
                "text_col": text_col,
            },
            remove_columns=remove_columns,
            load_from_cache_file=load_from_cache_file,
        )
    if verbose:
        print(dataset[0])
    return dataset
