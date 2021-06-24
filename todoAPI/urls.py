from django.urls import path
from . import views

urlpatterns = [
	path('read/',views.read),
	path('add/',views.add_task),
]