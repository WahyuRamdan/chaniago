from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate

def home(request):  
    maps = Maps.objects.all()
    crud = Crud.objects.all()

    return render(request, 'index.html', context = {
        "maps": maps,
        "crud" : crud
    })

def crud1(request):
    if request.method == "POST":
        Maps.objects.create(
            alamat = request.POST.get('alamat'),
            lokasi = request.POST.get('lokasi')
        )
        return redirect("/")

    return render(request, 'CRUD1.html')

def crud2(request):
    crud = Crud.objects.all()
    if request.method == "POST":
        Crud.objects.create(
            nama = request.POST.get('nama'),
            keterangan = request.POST.get('keterangan'),
            lokasi = request.POST.get('lokasi'),
        )
    return render(request, 'CRUD2.html', context = {
        "crud" : crud
    })

def crud2Update(request, id):
    crud = Crud.objects.all()
    update_crud = Crud.objects.get(id = id)

    if request.method == "POST":
        update_crud.nama = request.POST.get('nama')
        update_crud.keterangan = request.POST.get('keterangan')
        update_crud.lokasi = request.POST.get('lokasi')
        update_crud.save()
        
    return render(request, 'CRUD2.html', context = {
        "crud" : crud,
        "update_crud" : update_crud
    })

def crud2Hapus(request, id):
    update_crud = Crud.objects.get(id = id)
    update_crud.delete()
    return redirect("/CRUD2")

def login(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        user = authenticate(request, username = request.POST.get("username"), password = request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            return redirect("/")

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        u = User.objects.create(
            username = request.POST.get("username")
        )
        u.set_password( request.POST.get("password"))
        u.is_staff = True
        u.is_superuser = True
        u.save()
        return redirect("/")
    return render(request, 'register.html')

