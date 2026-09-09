#!/usr/bin/python

"""
import requests

from requests import session

payload = {
    'action': 'login',
    'username': USERNAME,
    'password': PASSWORD,
    'more_data' : "more data to send"
}

cookie = {'my_session': '17ab96bd8ffbe8ca58a78657a918558'}

with session() as c:
    #c.post('http://example.com/login', cookies=cookie, data=payload)
    request = c.get('http://example.com/protected_page', auth=('user', 'pass'))
    print request.headers
    print request.text


import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.json()



import urllib, json
url = 'https://github.com/timeline.json'
#url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
response = urllib.urlopen(url);
data = json.loads(response.read())
print data

"""

class SimpleClass(object):
    def get_name(self):
        return "SimpleClass"

    def key_method(self):
        return "key_method (SimpleClass)"


class MixIn1(object):
    def get_name(self):
        return "MixIn1" 

    def extra_method_1(self):
        return "extra_method_1 (MixIn1)" 

class MixIn2(object):
    def get_name(self):
        return "MixIn2"

    def extra_method_2(self):
        return "extra_method_2 (MixIn2)" 

class MixedClass(MixIn2, MixIn1, SimpleClass):
    def get_name(self):
        return "MixedClass"


c_1 = SimpleClass()
print c_1.get_name()

mixed = MixedClass()
print mixed.get_name()
print mixed.key_method()
print mixed.extra_method_1()
print mixed.extra_method_2()


------- Output ------------

SimpleClass
MixedClass
key_method (SimpleClass)
extra_method_1 (MixIn1)
extra_method_2 (MixIn2)


===============================

As an example, web pages can hold many ads, and an ad can be on many web pages.

from django.db import models

class WebPage(models.Model):
	url = models.CharField(max_length=256)
	
class Ad(models.Model):
    text = models.CharField(max_length=128)
    web_pages = models.ManyToManyField(WebPage)

# Make some web pages
w1 = WebPage(url='https://www.google.com')
w1.save()
w2 = WebPage(url='https://maps.google.com')
w2.save()

# Make some ads
a1 = Ad('Buy cool now')
a1.save()
a2 = Ad('Buy cooler right now')
a2.save()

# associate the ads to the web pages
a1.web_pages(w1)
a1.web_pages(w2)
a2.web_pages(w1, w2)


