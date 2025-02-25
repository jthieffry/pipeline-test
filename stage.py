from aws_cdk import Stage
from cdk_nag import NagSuppressions
from constructs import Construct

from core_stack import MyLambdaStack


class MyPipelineTestStage(Stage):
    def __init__(self, scope: Construct, id_: str):
        super().__init__(scope, id_)
        self.my_lambda_stack = MyLambdaStack(self, "MyLambdaStack")
        NagSuppressions.add_stack_suppressions(
            self.my_lambda_stack,
            suppressions=[{"id": "AwsSolutions-IAM4", "reason": "Not needed"}],
        )
