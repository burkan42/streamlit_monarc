import openml
import json

temp_res = openml.study.list_suites(status = 'all')

temp_res_list = []
temp_res_list_id = []
temp_res_list_name = []
temp_res_list_status = []

key_list = list(temp_res.keys())

for i in range(len(key_list)):
    current_key = key_list[i]
    current_value = temp_res[current_key]
    temp_res_list_id.append(current_value['id'])
    temp_res_list_name.append(current_value['name'])
    temp_res_list_status.append(current_value['status'])
    # Nog checken of status een interesante variabele is
# id, name, status
# TODO: for userinput ambition
# temp_res_list.append(temp_res_list_id)
# temp_res_list.append(temp_res_list_name)
# temp_res_list.append(temp_res_list_status)

temp_res_list = temp_res_list_name

print (json.dumps(temp_res_list))
    
# f = open("suites.txt", "w")
# f.write(str(temp_res_list))
# f.close()

# {'id': 253, 'alias': 'testecc18', 'main_entity_type': 'task', 'name': 'TesteCC18', 'status': 'in_preparation', 'creation_date': '2020-09-01 00:57:54', 'creator': 8598}