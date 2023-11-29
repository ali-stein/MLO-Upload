from django import template
from django.contrib.auth.models import Group
import re

register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
    
# https://www.abidibo.net/blog/2014/05/22/check-if-user-belongs-group-django-templates/
@register.filter(name='has_group')
def has_group(user, instructors):
    group = Group.objects.get(name=instructors)
    return True if group in user.groups.all() else False

"""
The MP4 file extension checker checks to see if the file extension
for the url is an .mp4 extension. If it is then it returns True. 
If it's not then it returns False.
"""
@register.filter(name='mp4_check')
def mp4_check(value, key):
    file = value.split(key)
    return file[1] == "mp4"

"""
The MP3 file extension checker checks to see if the file extension
for the url is an .mp3 extension. If it is then it returns True. 
If it's not then it returns False.
""" 
@register.filter(name='mp3_check')
def mp3_check(value, key):
    file = value.split(key)
    return file[1] == "mp3"

@register.filter(name="find_url")
def find_url(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    a = [x[0] for x in url]
    
    return a

# https://stackoverflow.com/questions/2295725/extending-urlize-in-django#2507447
@register.filter(name="url_target_blank", is_safe=True)
def url_target_blank(text):
    return text.replace('<a ', '<a target="_blank" ')