
import sys
import openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble, neighbors
import pandas as pd
from openml.datasets import edit_dataset, fork_dataset, get_dataset
from openml.tasks import TaskType
from openml.study import get_study
import webhook_listener
import time

openml.config.apikey = '6e8a64a5564e97f0f62f5bf6f18a4cd2'

#Argument_list = sys.argv[1:]
#Suite = Argument_list[0]
# suite type will come later
#Flow = Argument_list[1]
# flow type will come later
# ToDo: find id corresponding to above given name

study_id = 123
#flows_id = [7722, 7729]
flows_id = [7754, 7756]
task_id = [80, 23]
missing_tasks = []
#study_id = input()
#flows_id = input()
#2_flows_id = input()

def gatheringruns(study_id, flows_id):
    for i in flows_id:

        study = openml.study.get_study(study_id)

        evaluations = openml.evaluations.list_evaluations(
            function='predictive_accuracy', output_format='dataframe')

        for tasks in study.tasks:
            if tasks not in evaluations.task_id:
                missing_tasks.append(tasks)
                #run_missing = openml.runs.run_flow_on_task(task_id=tasks, flow=flows_id[0])
        # do something
        print('missing_tasks', missing_tasks)

        for i in flows_id:
            for j in missing_tasks:
                try:
                    print(f"Trying to run flow_id {i} on task {j}")
                    get_flow = openml.flows.get_flow(i, reinstantiate=True)
                    task_missing = openml.tasks.get_task(j)
                    run_missing = openml.runs.run_flow_on_task(flow=get_flow, task=task_missing)
                except ValueError:
                    print(f"flow_id {i} cant run on task {j}")
                else:
                    print("is succesful!")
        
    return missing_tasks


