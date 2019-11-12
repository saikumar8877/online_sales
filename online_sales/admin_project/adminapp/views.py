import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from adminapp.forms import MerchantRegisteForm
from .models import MerchantRegisteModel
from django.core.mail import send_mail
from admin_project import  settings as se
from django.contrib import messages
from django.views.generic import View
from django.core.serializers import serialize
from .forms import MerchantRegisteForm,ProductDetailsSavingForm


# Create your views here.
def mainpage(request):
    return render(request,'main.html')


def adminlogin(request):
    uname=request.POST.get('uname')
    password=request.POST.get('pwd')
    if uname=='admin' and  password=='admin' :
        return render(request,'adminwelcome.html')
    else:
        return render(request,'main.html',{'message':'Invalid User Details'})

def logoutAdmin(request):
    return render(request,'main.html')


def merchnat_login(request):
    return render(request,'adminwelcome.html',{'merchnatlogin':True})


def merchant_register(request):
    try:
        result=MerchantRegisteModel.objects.all()[::-1][0]
        merchantid=int(result.merchantid)+1
        return render(request,'adminwelcome.html',{'id':merchantid})
    except IndexError:
        merchantid=55018299
        return render(request,'adminwelcome.html', {'id': merchantid})


def addmerchant(request):
     return render(request,'adminwelcome.html',{'register1':True,})


def homepage(request):
    return render(request,'adminwelcome.html')


def savemerchant(request):
    rmid=request.POST.get('merchid')
    rname=request.POST.get('merchname')
    rcntno=request.POST.get('contno')
    remail=request.POST.get('email')
    pwd = rcntno[0] + str(int(rmid) + len(rname)) + rcntno[-1]
    pwd = remail[0] + pwd[:int(len(pwd) / 2)] + remail[1] + pwd[int(len(pwd) / 2):] + remail[2]
    MerchantRegisteModel(merchantid=rmid,merchantname=rname,contactno=rcntno,emailid=remail,password=pwd).save()
    subject="Online login details"
    message="Thank you for registering as Merchant, your user id is : "+ remail + " Password is : "+ pwd
    send_mail(subject,message,se.EMAIL_HOST_USER,[remail])
    messages.success(request,rname+"Registered successully")
    return merchant_register(request)


def viewMerchants(request):
    viewdetails=MerchantRegisteModel.objects.all()
    return render(request,'adminwelcome.html',{'viewdata':viewdetails})


def deletemerchant(request):
    rviewdetails=MerchantRegisteModel.objects.all()
    return render(request,'adminwelcome.html',{'viewdata1':rviewdetails})


def deletingMerchant(request):
    delmerch=request.GET.get('del_mech')
    MerchantRegisteModel.objects.filter(merchantid=delmerch).delete()
    return deletemerchant(request)


class CheckMechantLoginDetails(View):
    def get(self,request,email,pwd):
        try:
            res=MerchantRegisteModel.objects.get(emailid=email,password=pwd)
            json_data=serialize('json',[res])
            return HttpResponse(json_data,content_type='application/json',status=200)
        except MerchantRegisteModel.DoesNotExist:
            check={'notound':'Invalid user name and password'}
            json_data=json.dumps(check)
            return HttpResponse(json_data, content_type='application/json',status=500)

@method_decorator(csrf_exempt,name="dispatch")
class ChangingMerchantPassword(View):
    def put(self,request,email,pwd):
        try:
            old_data=MerchantRegisteModel.objects.get(emailid=email,password=pwd)
        except MerchantRegisteModel.DoesNotExist:
            data={'error_message':"Invaild login details" }
            json_info=json.dumps(data)
            return HttpResponse(json_info,content_type='application/json')
        else:
            # old_data is in object Format but we need in dict format
            # Converting object to dict
            old_data_dict={'merchantid':old_data.merchantid,
                           'merchantname':old_data.merchantname,
                           'contactno':old_data.contactno,
                           'emailid':old_data.emailid,
                           'password':old_data.password}
            data=request.body
            new_data=json.loads(data)
            # updating old data with new data
            old_data_dict.update(new_data)
            check=MerchantRegisteForm(old_data_dict,instance=old_data)

            if check.is_valid():
                check.save()
                d1={'message': "Password changed successully"}
                json_info=json.dumps(d1)
                return HttpResponse(json_info,content_type='application/json',status=200)
            if check.errors:
                json_info=json.dumps(check.errors)
                return HttpResponse(json_info, content_type='application/json')

@method_decorator(csrf_exempt,name='dispatch')
class SaveMerchantPdetails(View):
    def post(self,request):
        data=request.body
        res=json.loads(data)
        if not res:
            mess=json.dumps({'message':"invalid data"})
            return HttpResponse(mess,content_type='appliction/json',status=500)
        else:
            newdata=json.loads(data)
            form=ProductDetailsSavingForm(newdata)






