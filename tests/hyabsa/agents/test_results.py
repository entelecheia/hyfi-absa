from hyabsa.agents import AgentResult
from hyfi import HyFI


def test_results():
    # BaseAgent.generate_config()
    HyFI.generate_pipe_config(
        AgentResult.convert_absa_output_to_results,
        use_pipe_obj=False,
    )
    output_file = "tests/assets/predictions/output.jsonl"
    results = AgentResult.convert_absa_output_to_results(output_file)
    print(results[0])
    assert len(results) == 14
    results = AgentResult.convert_absa_output_to_results(output_file, skip_failed=True)
    assert len(results) == 13


if __name__ == "__main__":
    test_results()
