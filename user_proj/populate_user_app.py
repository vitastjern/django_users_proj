import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_proj.settings')

import django
django.setup()

# Populate with fake data!

import random

from user_app.models import User
from faker import Faker

fake = Faker()

def populate(N=10):
    for entry in range(N):
        #create the fake data for the entry

        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()
        print("First name:", fake_first_name, " Last name:", fake_last_name, " Email:", fake_email)
        user_rec = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print("Populating comlete!")

