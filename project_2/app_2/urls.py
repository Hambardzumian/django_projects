from django.urls import path
from .views import greeting, introduction, datetime,dictionary

urlpatterns = [
	path('',greeting,name="greeting"),
	path('introduction/',introduction, name="introduction"),
	path('datetime/', datetime, name="datetime"),
	path('dictionary/', dictionary , name="dictionary")
]