# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:02:13 2021

@author: bnkoz
"""

import sys
import openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble, neighbors
import pandas as pd
from openml.datasets import edit_dataset, fork_dataset, get_dataset
from openml.tasks import TaskType
from openml.study import get_study

openml.config.apikey = '6e8a64a5564e97f0f62f5bf6f18a4cd2'

#Argument_list = sys.argv[1:]
#Suite = Argument_list[0]
# suite type will come later
#Flow = Argument_list[1]
# flow type will come later
# ToDo: find id corresponding to above given name

study_id = 123
flows_id = [7722, 7729]
task_id = [80, 23]
#study_id = input()
#flows_id = input()
#2_flows_id = input()

tasks = openml.tasks.list_tasks(study_id)
#tasks = openml.study.list_studies(output_format='dataframe')

print(tasks)
#openml.runs.run_flow_on_task(flow=flows_id, task=)
evaluations = openml.evaluations.list_evaluations(
    function='predictive_accuracy', output_format='dataframe')

#evaluations = evaluations.pivot_table(index="data_id", columns="flow_id", values="value", aggfunc='first')
#evaluations.dropna()
