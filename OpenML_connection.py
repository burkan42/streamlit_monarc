
import openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble, neighbors
import pandas as pd
from openml.datasets import edit_dataset, fork_dataset, get_dataset
from openml.tasks import TaskType
from openml.study import get_study

def loadResults(study_id, flows_id):
    openml.config.apikey = '6e8a64a5564e97f0f62f5bf6f18a4cd2'
    #name of study
    study_name = openml.study.get_study(study_id)

    #gets evaluations of our tasks + flows
    def evals_by_id(study_id, flows_id):
        evaluations = openml.evaluations.list_evaluations(
            function='predictive_accuracy', study=study_id, flows=flows_id, output_format='dataframe')
        evaluations = evaluations.pivot_table(index="data_id", columns="flow_id", values="value", aggfunc='first')
        evaluations.dropna()
        return evaluations

    #calculates the percentage of outliers from diagplot
    def calc_diff(evaluations):
        evaluations['difference'] = evaluations[flows_id[0]]-evaluations[flows_id[1]]
        evaluations.dropna(inplace=True)
        percent_first_flow = (evaluations['difference']>0.2).sum()/evaluations['difference'].count()*100
        percent_second_flow = (evaluations['difference']<-0.2).sum()/evaluations['difference'].count()*100
        order_flow = {f'{flows_id[0]}':percent_first_flow, f'{flows_id[1]}':percent_second_flow }
        return(order_flow , evaluations)
    evaluations_id = evals_by_id(study_id,flows_id)
    order, evaluations_id= calc_diff(evaluations_id)

    #plot1
    plt.bar(order.keys(), order.values(), color=['red', 'blue'], width = 0.5)
    plt.ylabel("percentage of tasks significantly better (%)")
    plt.xlabel("flow ids")
    plt.title('Tasks significantly better in one flow (based on predictive accuracy)')
    plt.savefig("barplot.png")
    # TODO: save with descriptive name

    #plot2
    fig_splot, ax_splot = plt.subplots()
    ax_splot.plot(range(len(evaluations_id)), sorted(evaluations_id["difference"]))
    ax_splot.set_title(f"Difference between {study_name.name}")
    ax_splot.set_xlabel("Dataset (sorted)")
    ax_splot.set_ylabel(f"difference between {study_name.name}")
    ax_splot.grid(linestyle="--", axis="y")
    fig_splot.savefig("splot.png")
    # TODO: save with descriptive name

    #plot3
    fig_diagplot, ax_diagplot = plt.subplots()
    plt.title('predictive accuracy of both flows plotted against eachother')
    ax_diagplot.grid(linestyle="--")
    ax_diagplot.plot([0, 1], ls="-", color="black")
    ax_diagplot.plot([0.2, 1.2], ls="--", color="black")
    ax_diagplot.plot([-0.2, 0.8], ls="--", color="black")
    ax_diagplot.scatter(evaluations_id[flows_id[0]], evaluations_id[flows_id[1]])
    ax_diagplot.set_xlabel('predictive_accuracy flow id: '+ str(flows_id[0]))
    ax_diagplot.set_ylabel('predictive_accuracy flow id: '+ str(flows_id[1]))
    fig_diagplot.savefig("diagplot.png")
    # TODO: save with descriptive name

    splot = "<img src='splot.png' alt='plot' width='400px'>"
    barplot = "<img src='barplot.png' alt='plot' width='400px'>"
    diagplot = "<img src='diagplot.png' alt='plot' width='400px'>"
    graphs = [splot, barplot, diagplot]

    return evaluations_id
