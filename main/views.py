from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
       return render(request, 'index.html')


def page_handler(request, exception):
    return render(request, 'page_404.html')


def all_customer(request):
   customers =customer.objects.filter(delete=False)
   return render(request, 'customer list.html',{'customers':customers})

def single_customer(request,slug):
   cus =customer.objects.get(account_number=slug)
   return render(request, 'single customer.html',{'c':cus})


def account_statement(request,slug):
   user=customer.objects.get(account_number=slug)
   history =transcation.objects.filter(user=user)
   return render(request, 'customer history.html',{'history':history,'user':user})

@csrf_exempt
def transfer(request,slug):
   if request.method == "POST" and request.POST.get('amount'):
      amount=float(request.POST.get('amount'))
      receiver=request.POST.get('receiver')
      s=customer.objects.get(account_number=slug)
      if float(s.current_balance) >= amount:
          r=customer.objects.get(account_number=receiver)
          bal=float(r.current_balance) + amount
          dwn=float(s.current_balance) - amount
          dn = customer.objects.filter(account_number=slug).update(current_balance=dwn)
          up=customer.objects.filter(account_number=receiver).update(current_balance=bal)
          send_des='Amount Sent to '+r.full_name+' Acc No# '+r.account_number
          send=transcation(user=s,description=send_des,dr=amount,cr=0,balance=dwn)
          send.save()
          rec_des = 'Amount Received from ' + s.full_name + ' Acc No# ' + s.account_number
          rec=transcation(user=r,description=rec_des,cr=amount,dr=0,balance=bal)
          rec.save()
      return redirect('/all-customer')

   else:
     receiver =customer.objects.filter(delete=False)
     receiver =[c for c in receiver if c.account_number!=slug]
     sender =customer.objects.get(account_number=slug)
     return render(request, 'transfer money.html',{'receiver':receiver,'sender':sender})
