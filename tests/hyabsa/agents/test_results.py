from hyabsa.agents import AgentResult


def test_results():
    # BaseAgent.generate_config()
    output_file = "tests/assets/predictions/ouput.jsonl"
    results = AgentResult.convert_output_to_results(output_file)
    print(results[0])
    assert len(results) == 14
    results = AgentResult.convert_output_to_results(output_file, skip_failed=True)
    assert len(results) == 13


if __name__ == "__main__":
    test_results()
