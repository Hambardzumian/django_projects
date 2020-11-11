from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greeting(request):
	return HttpResponse("Hello I'am Hayk Hambardzumyan") 
def introduction(request):
	return HttpResponse(" This is my  first web cite")
def datetime(request):
	import datetime 
	return HttpResponse("{}".format(datetime.datetime.now()))
def dictionary(request):
	new_dict = {}
	for i in range(1,16):
		new_dict[i] = i**2
	return HttpResponse("{}".format(new_dict))
