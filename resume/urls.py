from django.urls import path
from resume.views import *
app_name = "resume"
urlpatterns = [
    path('', resume_view,name='index'),
]