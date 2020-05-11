import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project1.settings")

import django
django.setup()

from first_app.models import Users
from faker import Faker


fakegen = Faker()

def add_users(N):

    for i in range(N):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        mail = fakegen.email()
        u1 = Users.objects.get_or_create(first_name=fname, last_name=lname, email=mail)[0]
        u1.save()


if __name__ == "__main__":
    add_users(20)
    print("populate done!!!")