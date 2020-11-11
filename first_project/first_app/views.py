from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Hello DJango world !!!")
def last_name (request):
	return HttpResponse("I am Hayk Hambardzumyan")	
def ok(request):
	return render(request,"first_app/main.html")	
