from django import forms
from django.forms import ModelForm
from .models import Task
# Reordering Form and View

class CreateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    complete = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

 

class UpdateForm(forms.ModelForm):

    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    complete = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

 

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []