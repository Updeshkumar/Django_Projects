from django.shortcuts import render
from APIs.settings import ImagePath
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upload(request):
    if request.method=="POST":
        file = request.FILES['ufile']
        uploadedImg = str(file)
        imgPath = ImagePath
        with open(imgPath+uploadedImg, "wb") as desk:
            for chunk in file.chunks():
                desk.write(chunk)
            response = json.dumps([{"Success": "File Uploaded Success!"}])
            return HttpResponse(response, content_type = 'text/json')
        response = json.dumps([{"Error": "File Not Uploaded!"}])
        return HttpResponse(response, content_type = 'text/json')
    return HttpResponse("HelloWorld")
