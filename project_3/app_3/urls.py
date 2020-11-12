from django.urls import path
from .views import  task
urlpatterns = [
    # path('json/',json_read),
    path('task/',task),
]