import os

#this configures settings for the project
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project1.settings")


import django
django.setup()

import random
from first_app.models import Webpage,Topic,AccessRecord
from faker import Faker
fakegen = Faker()


topics = ['search','social','marketplace','news','games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        # get topic for entry
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=="__main__":
    print("populating data script")
    populate(20)
    print("population done")

