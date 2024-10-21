from bson.objectid import ObjectId

from django import template

register = template.Library()

def get_author(id_):
    return id_.id


register.filter('id', get_author)