from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from Home.models import Employee
def index(request):
    details = Employee.objects.all().values('id', 'name', 'address').order_by("-id")
    return render(request, 'list.html', {'details':details})
def delete(request,id):
    if request.method=="GET":
        Employee.objects.filter(id = id).delete()
        return redirect(reverse('index'))
def add(request):
    if request.method=="POST": 
        uname = request.POST.get('name')
        uaddress = request.POST.get('address')
        db = Employee(name = uname, address = uaddress)
        db.save()
        return redirect(reverse("index"))
    return render(request, 'add.html')
def edit(request, uid):
    db = Employee.objects.get(id = uid)
    name = db.name
    address = db.address
    if request.method=="POST": 
        uname = request.POST.get('name')
        uaddress = request.POST.get('address')
        data = Employee.objects.get(id = db.id)
        db.name = uname
        db.address = uaddress
        db.save()
        print(uaddress)
        return redirect(reverse("index"))
    return render(request, 'add.html', {'name':name, 'address':address})
    
    