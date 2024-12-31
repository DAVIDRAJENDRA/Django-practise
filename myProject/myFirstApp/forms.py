from django import forms
from myFirstApp.models import users_db

class NewUserForm(forms.ModelForm):

    class Meta():
        model = users_db
        fields = '__all__'