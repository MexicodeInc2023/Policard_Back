from django.contrib.admin import ModelAdmin, register
from .models import *


@register(User)
class studentAdmin(ModelAdmin):
   list_display = ('id', 'email','name','role','status','statuscredential')
   list_display_links = ('id',)
   actions = None
   filter_horizontal = ()