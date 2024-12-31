from django.shortcuts import render
from django.http import HttpResponse
from myFirstApp.models import users_db
from myFirstApp.forms import NewUserForm

def home(request):
    #webpages_list = AccessRecord.objects.order_by('date')
    #date_dict = {'access_records': webpages_list}
    user_list = users_db.objects.all()
    counts = len(user_list)
    date_dict = {'user_records': user_list, 'counts': counts}
    return render(request, "home.html", context= date_dict)

def secondPage(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'secondPage.html/', {'form':form})


    #returning data from model
    '''
    user_list = users_db.objects.all()
    date_dict = {'user_records': user_list}
    return render(request, "secondPage.html", context= date_dict)'''