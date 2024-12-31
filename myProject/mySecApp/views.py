from django.shortcuts import render
from mySecApp import forms

def index(request):
    return render(request, "mySecApp/index.html")

def forms_view(request):
    form = forms.sampleForm()

    if request.method == 'POST':
        form = forms.sampleForm(request.POST)

        if form.is_valid():
            print("Validation success!")

            print("name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])

    return render(request,"mySecApp/forms.html", {'form': form})