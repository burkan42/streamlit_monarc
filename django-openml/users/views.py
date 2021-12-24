from django.shortcuts import render, redirect
import document
import requests
# from document import getElementById
from .forms import MyForm
from users.functions import loadFlow, loadSuites
from users.OpenML_connection import loadResults
import json

def dashboard(request):
    # flow = list of flow names
    flow = loadFlow()
    # suit = list of suit names
    suit = loadSuites()
    


    if request.method == 'POST':
        form = MyForm(request.POST)
        
        if form.is_valid():
            print ("valid! from views.py")
            # for fieldname in form.cleaned_data:
            #     field = form.cleaned_data[fieldname]
            #     print(fieldname)
            #     print(field)
            # suite_id = form.cleaned_data['suite_id']
            # flow1 = form.cleaned_data['flow1']
            # flow2 = form.cleaned_data['flow2']
            # print(suite_id)
            # desc = suite_id

            # query = {'lat':'45', 'lon':'180'}
            # response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
            # responseData =response.json()['response']
            # for d in responseData:
            #     time = d['risetime']
            #     print("p")


            # pass data towards openML
            # TODO: get data from the ajax request
            data = request.POST.get('array[]')
            print("from views, data is =")
            print(data)
            array = data['array']
            print(array)
            output = loadResults(data)

            return render(request, "users/result.html", {'output':output})

    else:
        form = MyForm()
    return render(request, "users/dashboard.html",{'form':form,'flow':flow,'suit':suit})
    # 'desc':desc

def result(request):
    return render(request, "users/result.html")