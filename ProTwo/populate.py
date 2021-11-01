import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django

django.setup()

import random
from AppTwo.models import UserInfo
from faker import Faker

fake_gen = Faker()


def populate(N=5):
    for i in range(N):
        # get random name and mail id
        fake_fname = fake_gen.first_name()
        fake_lname = fake_gen.last_name()
        fake_mail = fake_gen.email()

        user_info = UserInfo.objects.get_or_create(
            fname=fake_fname, email=fake_mail, lname=fake_lname
        )


if __name__ == "__main__":
    print("Starting")
    populate(20)
    print("Ending")
