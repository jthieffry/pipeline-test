from typing import Mapping

from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(
    event: Mapping[str, int], context: LambdaContext | None
) -> Mapping[str, int]:
    input = event["initial_value"]
    return {"code": 200, "output": input + 5}
