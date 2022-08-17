import os
from pydoc_data.topics import topics
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')

import django
django.setup()

import random
from FirstApp.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social','Marketplace','News','Games']

def addTopic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):

        top = addTopic()
        fakeURL =  fakegen.url()
        fakeDate = fakegen.date()
        fakeName = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic = top, url = fakeURL, name = fakeName)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fakeDate)[0]

if __name__ == "__main__":
    print("Populating Script")
    populate(20) 
    print("complete!")       