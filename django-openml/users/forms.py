from django import forms
from django.forms import MultiWidget, TextInput


class MyForm(forms.Form):
	suite = forms.CharField()
	flow_1 = forms.CharField()
	flow_2 = forms.CharField()