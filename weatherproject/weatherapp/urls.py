from django.urls import path
from . import views
urlpatterns = [
    path('', views.home), #views.logoc-logic will be stored in the path
]
