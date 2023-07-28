import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# Fake Population script
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def create_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):

    for entry in range(N):
        # get the topic for entry
        topic = create_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        # create webpage
        webpage = Webpage.objects.get_or_create(topic=topic,url=fake_url,name=fake_name)[0]
        # create access records
        access_record = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print('Start Faker Script.....')
    populate(5)
    print('Completed Faker Script!')