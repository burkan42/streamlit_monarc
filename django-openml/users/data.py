from django.shortcuts import render
import document
# from document import getElementById
from .forms import MyForm

def array(request):
    form = MyForm(request.POST) 
    if form.is_valid():
        print ("valid! from data.py")
        for fieldname in form.cleaned_data:
            field = form.cleaned_data[fieldname]
            print(fieldname)
            print(field)

    # return render(request, "users/dashboard.html",{'form':form})
