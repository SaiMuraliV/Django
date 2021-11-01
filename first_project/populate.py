import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django

django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake_gen = Faker()
topics = ["search", "social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for itr in range(N):
        # get topic
        top = add_topic()
        # create fake for top
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # create an webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[
            0
        ]

        # fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)


if __name__ == "__main__":
    print("start")
    populate(20)
    print("end")
