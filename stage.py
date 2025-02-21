from aws_cdk import Stage
from constructs import Construct

from core_stack import MyLambdaStack


class MyPipelineTestStage(Stage):
    def __init__(self, scope: Construct, id_: str):
        super().__init__(scope, id_)
        MyLambdaStack(self, "MyLambdaStack")
