import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    add_page(cat=frame_cat,
         title="Flask",
         url="http://flask.pocoo.org",
         views=12)

    add_page(cat=frame_cat,
         title="Bottle",
         url="http://bottlepy.org/docs/dev/",
         views=5)

    django_cat = add_cat("Django", views=64, likes=32)

    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/",
             views = 7)

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/",
             views=6)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
             views=14)


    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/",
             views=5)


    add_page(cat=python_cat,
         title="How to Think like a Computer Scientist",
         url="http://www.greenteapress.com/thinkpython/",
         views=4)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/",
             views=7)

    python_pages = [
        {"title": "Official Python Tutorial",
        "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/"}, ]

    django_pages = [
        {"title": "Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
        "url":"http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
        "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
        "url":"http://flask.pocoo.org"} ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages} }



   # This did not work to make pages
   # Hence used method above

   #  for cat, cat_data in cats.iteritems():
   #      c = add_cat(cat)
   #      for p in cat_data["pages"]:
   #          add_page(c, p["title"], p["url"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title, url=url)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()