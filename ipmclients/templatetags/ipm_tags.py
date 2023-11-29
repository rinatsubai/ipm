from django import template
from ipmalpha.models import *
from ipmclients.models import *

register = template.Library()

# @register.simple_tag()
# def get_clients(filter=None):
#     if not filter:
#         return Client.objects.all()
#     else:
#         return Client.objects.filter(id=filter)

# @register.inclusion_tag()
# def get_clients(filter=None):
#     if not filter:
#         return Client.objects.all()
#     else:
#         return Client.objects.filter(id=filter)

# @register.simple_tag()
# def get_projects():
#     return Client.objects.all()
