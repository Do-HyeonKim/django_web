from django.urls import  path
from accountapp import views

app_name ='account'
urlpatterns = [
    path('hello_word', views.hello_word, name='hello_word')   
]
