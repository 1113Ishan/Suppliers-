from django.urls import path
from myapp.views import index
from myapp import views

app_name= "myapp"

urlpatterns = [
    path("myapp/", index)
]

