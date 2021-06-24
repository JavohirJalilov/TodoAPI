from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import db
def read(request):
	return JsonResponse(db.read())


def add_task(request):
	ID = db.count()
	print(ID)
	task_name = request.GET.get('name')
	task_description = request.GET.get('des')
	status = False
	db.addTask(ID,status,task_name,task_description)
	db.countUpdate(ID+1)
	return JsonResponse({"addTask":"Done✅"})