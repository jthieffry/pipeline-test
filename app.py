#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import Aspects
from cdk_nag import AwsSolutionsChecks

from stage import MyPipelineTestStage

app = cdk.App()
my_stage = MyPipelineTestStage(app, "MyStage")
Aspects.of(my_stage).add(AwsSolutionsChecks(verbose=True))

app.synth()
