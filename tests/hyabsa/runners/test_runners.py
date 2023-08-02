from hyabsa.runners import AbsaRunner


def test_absa_runner():
    runner = AbsaRunner()
    assert runner is not None
    AbsaRunner.generate_config()


def test_absa_runner_execute():
    runner = AbsaRunner(_config_name_="test")
    assert runner is not None
    print(runner.run())


if __name__ == "__main__":
    test_absa_runner()
    test_absa_runner_execute()
