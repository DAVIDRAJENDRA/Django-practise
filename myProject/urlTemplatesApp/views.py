from django.shortcuts import render

def base(request):
    return render(request, "urlTemplatesApp/base.html")

def relative(request):
    return render(request, "urlTemplatesApp/relative.html")