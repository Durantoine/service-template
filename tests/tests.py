from service import hello


def test_hello(sample_name: str) -> None:
    result = hello(sample_name)
    assert result == "Hello World"
