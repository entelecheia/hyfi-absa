from hyabsa.agents import BaseAgent


def test_base_agent():
    agent = BaseAgent
    assert agent is not None
    # BaseAgent.generate_config()


if __name__ == "__main__":
    test_base_agent()
