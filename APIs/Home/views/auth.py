from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

@csrf_exempt
def signup(request):
    if request.method=="POST":
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        upass = request.POST.get('psw')
        if uname is not None or uname!="":
            upass1 = make_password(upass)
            db = User(username = uemail, password = upass1, email = uemail, first_name = uname)
            try:
                db.save()
                response = json.dumps([{"success": "Acount Created Successfully!"}])
            except Exception as e:
                response = json.dumps([{"Error": "Something went Wrong!"}])
            return HttpResponse(response, content_type = 'text/json')
        response = json.dumps([{"NullValue": "Empty Data Found"}])
        return HttpResponse(response, content_type="text/json")
    return HttpResponse("Welcome Page")
@csrf_exempt           
def login(request):
    if request.method=="POST":
        uemail = request.POST.get('email')
        upass = request.POST.get('psw')
        print(uemail)
        user = auth.authenticate(username = uemail, password = upass)
        if user is not None:
            auth.login(request, user)
            response = json.dumps([{"Success":"Login Successfully!"}])
            return HttpResponse(response, content_type = "text/json")
        response = json.dumps([{"Error":"Invalid Crediantials!"}])
        return HttpResponse(response, content_type = "text/json")
    return HttpResponse("Login Page")
