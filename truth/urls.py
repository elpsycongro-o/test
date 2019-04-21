from django.urls import path
from . import views

app_name="truth"
urlpatterns=[
    path("",views.index,name="index"),
]
