from django.contrib.admin import ModelAdmin, register
from .models import *


@register(student)
class studentAdmin(ModelAdmin):
   list_display = ('id', 'user','id_emInfo','id_careers', 'personalName','lastname','birthday','grade','city','status','license', 'photo')
   list_display_links = ('id',)
   search_fields = ("user__name", "user__email")
   actions = None
   filter_horizontal = ()

@register(request_reason)
class request_reasondmin(ModelAdmin):
   list_display = ('id', 'id_st', 'reason','status',)
   list_display_links = ('id',)
   # search_fields = ("user__name", "user__email")
   actions = None
   filter_horizontal = ()
   
@register(emergency_info)
class emergency_infoAdmin(ModelAdmin):
   list_display = ('id', 'emergency_name','blood_type','status',)
   actions = None
   filter_horizontal = ()

@register(careers)
class careersAdmin(ModelAdmin):
   list_display = ('id', 'nameCareers', 'status','created_at','updated_at',)
   actions = None
   filter_horizontal = ()