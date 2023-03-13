from rest_framework.routers import DefaultRouter
from apps.users.views import *
from apps.credential.views import *

router = DefaultRouter()

router.register(r'student', studentView, basename='student')
router.register(r'careers', careersView, basename='careers')
router.register(r'emergency_info', emergency_infoView, basename='emergency_info')
router.register(r'request_reason', request_reasonView, basename='request_reason')



urlpatterns = router.urls