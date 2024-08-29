from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import smtplib
import datetime

def consumer_reg(request):
    if request.method == "POST":
        name = request.POST.get("conname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender = request.POST.get("humans")
        address = request.POST.get("address")
        password = request.POST.get("pwd")

        consumer.objects.create(Name = name, email = email, Phone = phone, Gender = gender, Password = password, Address = address)
        # Seller_reg.save()
        user = User.objects.create(username = email)
        user.set_password(password)
        user.save() 
    
        cdt=datetime.datetime.now()
        dt=cdt.strftime("%d %A %b %Y %I %M %S %p")    
    
        sender_email = "sv152801@gmail.com"
        Password = "mmrt athq cevm svoe"
        reciver_email = email

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()

        # for sender login
        server.login(sender_email, Password)
        
        server.sendmail(sender_email, reciver_email, f""" Hi {name},
                                Welcome !!
                                Your Account has Successfully created.
                                
                                Your email id : {email}
                                your password : {password}

                                Do not share your email id and password to others.                    
                                """)
        server.quit()
        return redirect("/cuslogin/")
    return render(request, "con_reg.html")


def view(request):

    people=consumer.objects.all()
    return render(request, "view.html",{"people": people})

def update(request,id):

    if request.method == "POST":

        user=get_object_or_404(consumer,S_No=id)
        user.Name = request.POST.get("conname")
        user.email = request.POST.get("email")
        user.Phone = request.POST.get("phone")
        user.Gender = request.POST.get("humans")
        user.Address = request.POST.get("address")
        user.Password = request.POST.get("pwd")
        user.save()
        
        return redirect("/view")

    upd=get_object_or_404(consumer,S_No=id)
    return render(request,"update.html",{"upd":upd})

def delete(request,id):
    person=get_object_or_404(consumer,S_No=id)
    person.delete()
    cdt=datetime.datetime.now()
    dt=cdt.strftime("%d %A %b %Y %I %M %S %p")    
    
    sender_email = "sv152801@gmail.com"
    Password = "mmrt athq cevm svoe"
    reciver_email = person.email

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

        # for sender login
    server.login(sender_email, Password)        
    server.sendmail(sender_email, reciver_email, f""" Hi {person.Name},
                                Welcome !!
                                Your Account has Successfully deleted.""")
    server.quit()
    
    return redirect("/view")


def con_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        user1 = authenticate(request, username = email, password = password)
        if user1 is not None:
            
            login(request, user1)
            cus=get_object_or_404(consumer,email = email)
            cdt=datetime.datetime.now()
            dt=cdt.strftime("%d %A %b %Y %I %M %S %p")    
            sender_email = "sv152801@gmail.com"
            Password = "mmrt athq cevm svoe"
            reciver_email = email

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()

            # for sender login
            server.login(sender_email, Password)
        
            server.sendmail(sender_email, reciver_email, f""" Hi {cus.Name},
                                    You had Loged in to your account. Welcome !!
                            Login time:{dt}""")
            server.quit()
            # cus=get_object_or_404(consumer,email = email)
            datas=products.objects.all()
            return render (request, "home.html", {"cus":cus, "datas":datas})
    
    return render(request,"con_login.html")
    

def con_logout(request, email):
    cus=get_object_or_404(consumer, email = email)
    logout(request)
    cdt=datetime.datetime.now()
    dt=cdt.strftime("%d %A %b %Y %I %M %S %p")
    sender_email = "sv152801@gmail.com"
    Password = "mmrt athq cevm svoe"
    reciver_email = email

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

            # for sender login
    server.login(sender_email, Password)
        
    server.sendmail(sender_email, reciver_email, f""" Hi {cus.Name},
                                    You had been Logged out from your account. Visit Again!!
                    Logut Time: {dt}""")
    server.quit()
    return HttpResponse("logged out.")


def searchbar(request,email):

    if request.method == "POST":
        search = request.POST.get("search")
        print(search)
        ind=get_object_or_404(consumer,email = email)
        things=products.objects.filter(Product = search)

        if things is not None:
            return render(request,"stores.html", {"things":things, "ind":ind })
        else:
            return HttpResponse("Product tempravaryly not available")
    
    return HttpResponse("Not valid.")


def buying(request,no,cemail):
    
    prd=get_object_or_404(products,No = no)
    prd.Seller_email
    slr=get_object_or_404(Seller_reg,Seller_email = prd.Seller_email)
    hum=get_object_or_404(consumer,email = cemail)
    
    if request.method == "POST":
        quant= request.POST.get("qty")
        amount=int(prd.Price) * int(quant)
        
        return render(request, "confirm.html",{"quant":quant, "amount": amount,"prd":prd , "slr":slr, "hum":hum})
    
    
     
    return render(request, "buy.html", {"prd":prd ,"slr":slr, "hum":hum})


def final(request,no,cons,qty,amt):

    if request.method == "POST":

        prd=get_object_or_404(products,No = no)
        slr=get_object_or_404(Seller_reg,Seller_email = prd.Seller_email)
        hum=get_object_or_404(consumer,email = cons)
      
        buyer.objects.create(buyerid = hum, sellerid = slr.S_No, Seller_name =slr.Seller_name ,Seller_address = slr.Address,product_name = prd.Product, product_image = prd.product_Photo, quantity = qty, rate = amt, seller_contact_number = slr.Phone, seller_email_id = slr.Seller_email)
        people=buyer.objects.filter(buyerid = hum.S_No)

        for i in people:
            print(i)
        
        sender_email = "sv152801@gmail.com"
        Password = "mmrt athq cevm svoe"
        reciver_email = hum.email

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()

        # for sender login
        server.login(sender_email, Password)
        
        server.sendmail(sender_email, reciver_email, f""" Hi {hum.Name},
                                Your order has been successfully Placed.It will arrive from two days of booking.
                        
                    Your product name: {prd.Product}.
                    Booked date: {i.buyeddate}, 
                                                        
                    your invoice is sent to email. Any doubts contactus through given email and contact number in invoice.
                                                        
                                    Thank you. visit us Always.""")
        server.quit()
        msg = "order placed success."
        return render (request, "result.html", {"msg":msg, "cus":hum})
    
    return HttpResponse ("not")   

def pview(request,pno,cemail):

    prd=get_object_or_404(products,No = pno)
    slr=get_object_or_404(Seller_reg, Seller_email = prd.Seller_email)
    hum=get_object_or_404(consumer,email=cemail)

    return render(request, "pview.html", {"prd":prd, "slr":slr, "hum":hum })

def my_purchase(request, email):
    cus=get_object_or_404(consumer,email = email)
    my=buyer.objects.filter(buyerid=cus.S_No)
    return render(request, "buyedproducts.html",{"my":my , "cus":cus})

def about(request):
    return render(request,"about.html")

