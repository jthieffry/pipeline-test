import aws_cdk.pipelines as cdk_pipelines
from aws_cdk import Stack
from constructs import Construct


class MyPipeline(Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs):
        super().__init__(scope, id_, **kwargs)

        self.my_pipeline = cdk_pipelines.CodePipeline(
            self,
            "MyPipeline",
            synth=cdk_pipelines.ShellStep(
                "Synth",
                input=cdk_pipelines.CodePipelineSource.connection(
                    repo_string="jthieffry/pipeline-test",
                    branch="main",
                    connection_arn="arn:aws:codeconnections:us-east-1:205930626365:connection/4772fc69-cd82-4cad-89ad-13a6545a5bc6",
                ),
                install_commands=[
                    "curl -LsSf https://astral.sh/uv/install.sh | sh",
                    "export PATH=$PATH:/root/.local/bin",
                    "uv sync",
                    "npm install -g aws-cdk",
                ],
                commands=["cdk synth"],
            ),
        )
