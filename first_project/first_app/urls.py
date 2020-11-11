from django.urls import path
from .views import home, last_name, ok

urlpatterns = [
	path('', home, name="home"),
	path('last_name/',last_name, name="last_name"),
	path('ok/',ok, name="ok"),

]