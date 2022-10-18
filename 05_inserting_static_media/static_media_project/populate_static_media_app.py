import imp
import os
# this is just basically configuring the settings for the project
# you need to do this before manipulating the models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'static_media_project.settings')

import django
# this should setup and configure the project settings
django.setup()

## Fake population script
import random
from static_media_app.models import Topic, Webpage, AccessRecord
from faker import Faker
# faker is not working ?

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    # this is going to retrieve the 
    # topic if it already exists, 
    # otherwise it'll create it
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()
        # create the fake data for that entry
        # you can create a lot of fake data from calling .___() - explore the docs for more info
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name )[0]
        # [0] grab the first object in the tuple thats returned

        # create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=Webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')

# > python populate_static_media_app.py