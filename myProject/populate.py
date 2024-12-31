import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
import django
django.setup()
import random
from faker import Faker
from myFirstApp.models import users_db


fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        userss = users_db.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(25)
    print("populating compleate!")