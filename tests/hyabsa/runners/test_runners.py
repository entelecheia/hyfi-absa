from hyabsa.runners import AbsaRunner


def test_absa_runner():
    runner = AbsaRunner()
    assert runner is not None
    print(AbsaRunner.generate_config())


if __name__ == "__main__":
    test_absa_runner()
