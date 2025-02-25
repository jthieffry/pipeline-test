#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import Aspects
from cdk_nag import AwsSolutionsChecks

from pipeline import MyPipeline
from stage import MyPipelineTestStage

app = cdk.App()
top_pipeline = MyPipeline(app, "MyTopPipeline")
my_stage = MyPipelineTestStage(top_pipeline, "MyStage")
Aspects.of(my_stage).add(AwsSolutionsChecks(verbose=True))
top_pipeline.my_pipeline.add_stage(my_stage)

app.synth()
