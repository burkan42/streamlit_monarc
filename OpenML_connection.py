import sys
import openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble, neighbors
import pandas as pd
from openml.datasets import edit_dataset, fork_dataset, get_dataset
from openml.tasks import TaskType

def loadResults(study_id, flows_id):

    # suit = data[0]
    # print("benchmarksuite = " + suit)
    # i = 1
    # while (i in data):
    #     # {do something with flowpair}
    #     print(data[i])
    #     print("flow pair number = " + i)
    #     print("flows in current flow pair = ")
    #     print (data[i][0])
    #     print (data[i][1])

    # print("reached openMLfunction")
    openml.config.apikey = '6e8a64a5564e97f0f62f5bf6f18a4cd2'
    #study_id = 123
    #flows_id = [7722, 7729]
    # TODO: gebruik Suite, Flow1, Flow2
    # flow type will come later
    # TODO: find id corresponding to above given name   

    def evals_by_id(study_id, flows_id):
        evaluations = openml.evaluations.list_evaluations(
            function='predictive_accuracy', study=study_id, flows=flows_id, output_format='dataframe')
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

    plt.bar(order.keys(), order.values(), color=['red', 'blue'], width = 0.5)
    plt.ylabel("# of tasks")
    plt.title('performance flow_ids on # of tasks')
    plt.savefig("barplot.png")
    # TODO: save with descriptive name

    fig_splot, ax_splot = plt.subplots()
    ax_splot.plot(range(len(evaluations_id)), sorted(evaluations_id["difference"]))
    ax_splot.set_title('Difference non-linear and linear classifier')
    ax_splot.set_xlabel("Dataset (sorted)")
    ax_splot.set_ylabel("difference between linear and non-linear classifier")
    ax_splot.grid(linestyle="--", axis="y")
    fig_splot.savefig("splot.png")
    # TODO: save with descriptive name

    fig_diagplot, ax_diagplot = plt.subplots()
    ax_diagplot.grid(linestyle="--")
    ax_diagplot.plot([0, 1], ls="-", color="black")
    ax_diagplot.plot([0.2, 1.2], ls="--", color="black")
    ax_diagplot.plot([-0.2, 0.8], ls="--", color="black")
    ax_diagplot.scatter(evaluations_id[flows_id[0]], evaluations_id[flows_id[1]])
    ax_diagplot.set_xlabel('predictive_accuracy')
    ax_diagplot.set_ylabel('predictive_accuracy')
    fig_diagplot.savefig("diagplot.png")
    # TODO: save with descriptive name

    splot = "<img src='splot.png' alt='plot' width='400px'>"
    barplot = "<img src='barplot.png' alt='plot' width='400px'>"
    diagplot = "<img src='diagplot.png' alt='plot' width='400px'>"
    graphs = [splot, barplot, diagplot]

    return evaluations_id

# Argument_list = sys.argv[1:]
# Suite = Argument_list[0]
# Flow1 = Argument_list[1]
# Flow2 = Argument_list[2]

# loadResults(Suite, Flow1, Flow2)