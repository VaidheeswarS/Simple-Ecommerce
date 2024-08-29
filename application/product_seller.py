from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def product_salers(request):
    
    if request.method == "POST":

        name = request.POST.get("salname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender = request.POST.get("humans")
        address = request.POST.get("address")
        password = request.POST.get("pwd")
        photo = request.POST.get("photo")

        Seller_reg.objects.create(Seller_name = name, Seller_email = email, Phone = phone, Gender = gender, Password = password, Address = address, Photo = photo)
        # Seller_reg.save() #
        user=User.objects.create(username=email)
        user.set_password(password)
        user.save()

        return HttpResponse("sucess.")
    return render(request,"pro_sal_registration.html")


def pro_sal_view(request):
    datas=Seller_reg.objects.all()
    return render(request,"pro_sal_view.html",{"datas":datas})

def update_sal(request,id):
    if request.method == "POST":
        user=get_object_or_404(Seller_reg,S_No=id)
        user.Seller_name = request.POST.get("salname")
        user.Seller_email = request.POST.get("email")
        user.Phone = request.POST.get("phone")
        user.Gender = request.POST.get("humans")
        user.Address = request.POST.get("address")
        user.Password = request.POST.get("pwd")
        user.Photo = request.POST.get("photo")
        user.save()
        
        return redirect("/selview")

        # Seller_reg.objects.create(Seller_name = name, Seller_email = email, Phone = phone, Gender = gender, Password = password, Address = address, Photo = photo)
        # Seller_reg.save()

    uservalue=get_object_or_404(Seller_reg,S_No=id)
    return render(request, "sal_update.html", {"uservalue": uservalue})


def delete_sal(request,id):
    if request.method == "POST":
        pers=get_object_or_404(Seller_reg,S_No=id)
        pers.delete()
        return redirect("/selview")

    return render (request, "delete_sal.html")

