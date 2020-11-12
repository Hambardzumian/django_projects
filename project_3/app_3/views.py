from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import random


# Create your views here.\
def index (request):
	return render(request,'app_3/main.html')
# def json_read(request):
#     with open('{}\\app_3\\main.json'.format(os.getcwd()), 'r') as file:
#     	json_text = json.load(file)
#     	text_starting = "Dictionary is----{}".format(json_text)
#     	main_html = '''
#     <title>Json make readable</title>
#     <body style=\"background-color:#B179F1\">
#         <a href= \"http://127.0.0.1:8000/\" style=\"color:#512089\">Back</a>
#         <h1 style=\"color:#512089\">Json to Readable</h1>
#         <h3  style=\"color:#512089\">Program succassfully finished reading json file</h3>
#         <h3  style=\"color:#512089\">{}</h3>
#     <body>
#     '''.format(text_starting)
#     return HttpResponse(main_html)
def check (request):
	return render(request, 'app_3/check.html')
def task (request):
	d = {}
	d1 = {'a': 100, 'b': 200, 'c':300}
	d2 = {'a': 300, 'b': 200, 'd':400}
	for i in d1:
		if i in d2:
			d[i] = d1[i] + d2[i]
		else:
			d[i] = d1[i]
	for i in d2:			
		d[i] = d2[i]
	return HttpResponse("{}".format(d))		

