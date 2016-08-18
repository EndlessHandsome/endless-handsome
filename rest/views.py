from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer 
from rest.models import User
from rest.serializer import UserSerializer

# Create your views here.
class JsonResponse(HttpResponse):
 	def __init__(self, data,**kwargs):
 		content = JSONRenderer().render(data)
 		kwargs['content_type'] = 'application/json'
 		super(JsonResponse, self).__init__(content,**kwargs)

def userlist(req):
	if req.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users,many=True)
		return JsonResponse(serializer.data)

	if req.method == 'POST':
		data = JsonParser().parse(req)
		serializer = UserSerializer(data.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.error,status=400)

def user_name(req,name):
	try:
		user = User.objects.get(username=name)
	except User.DoesNotExist:
		return HttpResponse(status=404)

	if req.method == 'GET':
		serializer = UserSerializer(user)
		return JsonResponse(serializer.data)

	elif req.method == 'POST':
		data = JsonParser(req.data)
		serializer = UserSerializer(data.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.error,status=400)

	elif req.method == 'DELETE':
		user.delete()
		return HttpResponse(status=204)