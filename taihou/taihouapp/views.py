from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from taihouapp.tencent import CheckAccount, AddAccount, AutoLogin
from taihouapp.models import Account

# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def check(request):
    Name=request.POST['Name']
    if CheckAccount(Name)==0:
        return HttpResponse(Name+"@taihou.moe is still available !")
    else:
        return HttpResponse('Sorry, '+Name+'@taihou.moe already exists...')

@csrf_exempt
def create(request):
    Name=request.POST['Name']
    if AddAccount(Name):
        return HttpResponse('Success! Click here to login your account now!')
    else:
        return HttpResponse("Oops! There's something wrong while creating...")

@csrf_exempt
def login(request):
    Name=request.POST['Name']
    try:
        User=Account.objects.get(AccountName=Name.lower())
        if User.LoginAuth:
            User.LoginAuth=False
            User.save()
            return HttpResponse(AutoLogin(Name))
        else:
            return HttpResponse("Exist")
    except:
        return HttpResponse('Error')

def autologin(request):
    auth=request.GET['auth']
    Name=request.GET['Name']
    return HttpResponseRedirect("https://exmail.qq.com/cgi-bin/login?fun=bizopenssologin&method=bizauth&agent=476458427&user="+Name+"@taihou.moe&ticket="+auth)
