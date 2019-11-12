from django.shortcuts import render,redirect
from django.views.generic import View
import requests
import json
from django.contrib import messages
# Create your views here.


def merchnatlogin(request):
    return render(request,'merchantlogin.html')

def checkLogin(request):
     email=request.POST.get('uid')
     password=request.POST.get('mpwd')
     try:
         value=request.session['merchantid']
         res=requests.get('http://192.168.43.143:8000/checklogin/'+email+'&'+password+'/')
         if res.status_code == 200:
             json_data = res.json()
             return render(request,'merchantlogged.html',{"data":json_data})
         else:
             messages.error(request,'Invalid Username Details')
             return redirect('login')
     except requests.exceptions.ConnectionError:
         messages.error(request, 'Server Not Available')
         return redirect('login')


def changeMechantPassword(request):
     email=request.POST.get('email')
     old_password=request.POST.get('old_password')
     new_password=request.POST.get('new_password1')
     confirm_password=request.POST.get('new_password2')
     # print(email)
     # print(old_password)
     # print(new_password)
     # print(confirm_password)
     if new_password == confirm_password:
         datasending=json.dumps({'password':new_password})
         try:
             change=requests.put('http://192.168.43.143:8000/changingpassword/'+email+'&'+old_password+'/',data=datasending)

         except requests.exceptions.ConnectionError :
             messages.error(request,'server not available')
             return redirect('change')
         else:
             if change.status_code==200:
                 json_data = change.json()
                 return render(request, 'changepassword.html', {'data': json_data})
             else:
                 messages.error(request,'Invalid user details')
                 return redirect('change')
     else:
         messages.error(request,'New and confirm Password Mis-Match')
         return redirect('change')


def backmerchankpage(request):
    return render(request,'merchantlogin.html')


def changingpage(request):
    return render(request,'changepassword.html')


def savingProductDetails(request):
    productid=request.POST.get('pid')
    productname=request.POST.get('pname')
    productprice=request.POST.get('pprice')
    productquantity=request.POST.get('pquantity')
    productd1={'productid':productid,'name':productname,'price':productprice,'quantity':productquantity}
    send_data=json.dumps(productd1)
    try:
        result=requests.post('http://192.168.43.143:8000/saving_product_details/',data=send_data)
    except requests.exceptions.ConnectionError:
        messages.error(request,"server not available")
        return redirect('checklogin')


