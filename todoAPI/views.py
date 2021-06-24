from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import db
def read(request):
	return JsonResponse(db.read())
