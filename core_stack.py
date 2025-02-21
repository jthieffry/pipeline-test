from aws_cdk import Stack
from aws_cdk.aws_lambda import Code, Function, LayerVersion, Runtime
from constructs import Construct


class MyLambdaStack(Stack):
    def __init__(self, scope: Construct, id_: str):
        super().__init__(scope, id_)

        powertools_layer = LayerVersion.from_layer_version_arn(
            self,
            "PowertoolsLayer",
            layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:8",
        )

        Function(
            self,
            "MyFunction",
            code=Code.from_asset("./assets/SimpleLambda"),
            runtime=Runtime.PYTHON_3_12,
            handler="lambda_function.handler",
            layers=[powertools_layer],
        )
