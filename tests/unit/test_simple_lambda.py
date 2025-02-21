from assets.SimpleLambda import lambda_function


def test_correct_output() -> None:
    assert lambda_function.lambda_handler({"initial_value": 2}, None) == {
        "code": 200,
        "output": 7,
    }
