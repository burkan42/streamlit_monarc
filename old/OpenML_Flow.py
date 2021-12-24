import openml
from openml.tasks import TaskType
import openml.datasets
import openml.runs
import openml.flows
import openml.study
import json
# Dataset part:
temp_res = openml.flows.list_flows()
# 1- 19410

temp_res_list = []
temp_res_list_id = []
temp_res_list_name = []
temp_res_list_version = []

key_list = list(temp_res.keys())


for i in range(len(key_list)):
    current_key = key_list[i]
    current_value = temp_res[current_key]
    temp_res_list_id.append(current_value['id'])
    temp_res_list_name.append(current_value['name'])
    temp_res_list_version.append(current_value['version'])

# id, name, version
# TODO: for userinput ambition
# temp_res_list.append(temp_res_list_id)
# temp_res_list.append(temp_res_list_name)
# temp_res_list.append(temp_res_list_version)

temp_res_list = temp_res_list_name
print (json.dumps(temp_res_list))

# f = open("Flow.txt", "w")
# f.write(str(temp_res_list))
# f.close()

# current_value outputs is formatted like a dict:
# {'id': 8, 'full_name': 'openml.evaluation.class_complexity(1.0)', 'name': 'openml.evaluation.class_complexity', 'version': '1', 'external_version': None, 'uploader': '1'}
# this is a list of dict