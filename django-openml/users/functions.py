import sys
import openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble, neighbors
import pandas as pd
from openml.datasets import edit_dataset, fork_dataset, get_dataset
from openml.tasks import TaskType
import streamlit as st
import js2py

@st.cache
def loadFlow():
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
    # temp_res_list.append(temp_res_list_id)
    # temp_res_list.append(temp_res_list_name)
    # temp_res_list.append(temp_res_list_version)

    temp_res_list = temp_res_list_name
    # print (json.dumps(temp_res_list))
    return temp_res_list

    # f = open("Flow.txt", "w")
    # f.write(str(temp_res_list))
    # f.close()

@st.cache
def loadSuites():
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

    # temp_res_list.append(temp_res_list_id)
    # temp_res_list.append(temp_res_list_name)
    # temp_res_list.append(temp_res_list_status)

    temp_res_list = temp_res_list_name

    # print (json.dumps(temp_res_list))
    return temp_res_list
        
    # f = open("suites.txt", "w")
    # f.write(str(temp_res_list))
    # f.close()

@st.cache
def loadResults(Suite, Flow1, Flow2):

    openml.config.apikey = '6e8a64a5564e97f0f62f5bf6f18a4cd2'

    Argument_list = sys.argv[1:]
    Suite = Argument_list[0]
    # suite type will come later
    Flow1 = Argument_list[1]
    Flow2 = Argument_list[2]
    # flow type will come later
    # ToDo: find id corresponding to above given name

    study_id = 123
    flows_id = [7722, 7729]
    class_values = ["non-linear better", "linear better", "equal"]
    measure = "predictive_accuracy"
    classifier_family = "SVM"
    meta_features = ["NumberOfInstances", "NumberOfFeatures"]
    #study_id = input()
    #flows_id = input()
    #2_flows_id = input()


    def evals_by_id(study_id, flows_id):
        evaluations = openml.evaluations.list_evaluations(
            function='predictive_accuracy', study=study_id,flows=flows_id, output_format='dataframe')
        print(evaluations)
        evaluations = evaluations.pivot_table(index="data_id", columns="flow_id", values="value", aggfunc='first')
        evaluations.dropna()

        return evaluations

    def calc_diff(evaluations):
        evaluations['difference'] = evaluations[flows_id[0]]-evaluations[flows_id[1]]
        evaluations.dropna(inplace=True)
        
        number_first_flow = (evaluations['difference']>0).sum()
        number_second_flow = (evaluations['difference']<0).sum()
        Tot_Tasks = evaluations['difference'].count()
        order_flow = {f'{flows_id[0]}':number_first_flow, f'{flows_id[1]}':number_second_flow }
        return(order_flow, Tot_Tasks, evaluations)

    evaluations_id = evals_by_id(study_id,flows_id)
    order, total, evaluations_id= calc_diff(evaluations_id)

    def determine_class(val_lin, val_nonlin):
        if val_lin < val_nonlin:
            return class_values[0]
        elif val_nonlin < val_lin:
            return class_values[1]
        else:
            return class_values[2]
        
    data_qualities = openml.datasets.list_datasets(
        data_id=list(evaluations_id.index.values), output_format="dataframe"
    )

    data_qualities = data_qualities[meta_features]
    # makes a join between evaluation table and data qualities table,
    # now we have columns data_id, flow1_value, flow2_value, meta_feature_1,
    # meta_feature_2
    evaluations = evaluations_id.join(data_qualities, how="inner")

    evaluations_id["class"] = evaluations_id.apply(
        lambda row: determine_class(row[flows_id[0]], row[flows_id[1]]), axis=1
    )

    # does the plotting and formatting
    fig_scatter, ax_scatter = plt.subplots()

    for class_val in class_values:
        df_class = evaluations_id[evaluations_id["class"] == class_val]
        plt.scatter(df_class[meta_features[0]], df_class[meta_features[1]], label=class_val)


    ax_scatter.set_title(classifier_family)
    ax_scatter.set_xlabel(meta_features[0])
    ax_scatter.set_ylabel(meta_features[1])
    ax_scatter.legend()
    ax_scatter.set_xscale("log")
    ax_scatter.set_yscale("log")
    # plt.show()

    plt.bar(order.keys(), order.values(), color=['red', 'blue'], width = 0.5)
    plt.ylabel("# of tasks")
    plt.title('performance flow_ids on # of tasks')
    plt.savefig("barplot.png")
    # print(plt.show())

    fig_splot, ax_splot = plt.subplots()
    ax_splot.plot(range(len(evaluations_id)), sorted(evaluations_id["difference"]))
    ax_splot.set_title('Difference non-linear and linear classifier')
    ax_splot.set_xlabel("Dataset (sorted)")
    ax_splot.set_ylabel("difference between linear and non-linear classifier")
    ax_splot.grid(linestyle="--", axis="y")
    fig_splot.savefig("splot.png")
    # print(plt.show())

    fig_diagplot, ax_diagplot = plt.subplots()
    ax_diagplot.grid(linestyle="--")
    ax_diagplot.plot([0, 1], ls="-", color="black")
    ax_diagplot.plot([0.2, 1.2], ls="--", color="black")
    ax_diagplot.plot([-0.2, 0.8], ls="--", color="black")
    ax_diagplot.scatter(evaluations_id[flows_id[0]], evaluations_id[flows_id[1]])
    ax_diagplot.set_xlabel('predictive_accuracy')
    ax_diagplot.set_ylabel('predictive_accuracy')
    fig_diagplot.savefig("diagplot.png")
    # print(plt.show())

    output = "<img src='splot.png' alt='plot' width='400px'>  <img src='barplot.png' alt='plot' width='400px'> <img src='diagplot.png' alt='plot' width='400px'>"
    # print("<img src='splot.png' alt='plot' width='400px'>")
    # print("<img src='barplot.png' alt='plot' width='400px'>")
    # print("<img src='diagplot.png' alt='plot' width='400px'>")
    return output

# Flow = loadFlow()
# Suit = loadSuites()

# st.title('OpenML Mythbusting')
# with st.form("my_form"):
#     print('<div class="autocomplete" style="width:300px;">')
#     st.subheader('Please select your Benchmark suit')
#     st.text_input('Benchmark', key='Benchmark')
#     if 'Benchmark' not in st.session_state:
#       print("Benchmark not in session state")
#       st.session_state['Benchmark'] = 'Benchmark-value'

#     st.subheader('Please select your flows')
#     st.text_input('flow1', key='flow1')
#     if 'flow1' not in st.session_state:
#       print("flow1 not in session state")
#       st.session_state['flow1'] = 'flow1-value'

#     st.text_input('flow2', key='flow2')
#     if 'flow2' not in st.session_state:
#       print("flow2 not in session state")
#       st.session_state['flow2'] = 'flow2-value'

#     eval_res, tempfile = js2py.run_file("main.js")
#     tempfile.autocomp(st.session_state['flow1'], Flow)
#     tempfile.autocomp(st.session_state['flow2'], Flow)
#     tempfile.autocomp(st.session_state['Benchmark'], Suit)

#     st.subheader('Please click submit when your done selecting the parameters')
#     submitted = st.form_submit_button("Submit")
#     # , on_click= loadResults
#     st.text('that was the submit button?')
#     print('</div>')
    
#     if submitted:
#       st.write("suit", st.session_state['Benchmark'], "flow1", st.session_state['flow1'], "flow2", st.session_state['flow2'])
#       st.write(loadResults(st.session_state['Benchmark'], st.session_state['flow1'], st.session_state['flow2']))