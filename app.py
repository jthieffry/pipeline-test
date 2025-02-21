#!/usr/bin/env python3
import aws_cdk as cdk

from stage import MyPipelineTestStage

app = cdk.App()
MyPipelineTestStage(app, "MyStage")

app.synth()
