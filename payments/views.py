from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
from requests.auth import HTTPBasicAuth
import json, uuid
from .models import QR
from .credentials import MpesaAccessToken, LipanaMpesaPpassword
from .forms import transactionsForm
from qr_pay.settings import env

# Create your views here.
def getAccessToken(request):
    consumer_key = env('CONSUMER_KEY')
    consumer_secret = env('CONSUMER_SECRET')
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request, id, contact):
    idcov = uuid.UUID(id)
    trx = QR.objects.get(uuid=idcov)
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {       
        "BusinessShortCode": "174379", 
        "Password": LipanaMpesaPpassword.decode_password, 
        "Timestamp": LipanaMpesaPpassword.lipa_time, 
        "TransactionType": "CustomerPayBillOnline", 
        "Amount": trx.amount, 
        "PartyA": contact,# replace with your phone number to get stk push
        "PartyB": "174379",    
        "PhoneNumber": contact, # replace with your phone number to get stk push
        "CallBackURL": "https://posthere.io/1bfa-4202-9fb6",       
        "AccountReference": "Transport: " + trx.route,
        "TransactionDesc": "Testing stk push"
    } 
    
    response = requests.post(api_url, json=request, headers=headers)
 
    return HttpResponse("Success")

def home(request): 
        qrs = QR.objects.all()
        return render(request, 'home/index.html', {'qrs':qrs})

def logout_view(request):
    logout(request)
    return redirect('/admin')
      
class paymentView(TemplateView): 
    template_name = 'home/pay.html'
    # get function # get qr model objects from database
    def get(self, request, id):        
        qr = QR.objects.get(uuid=id)
        return render(request, self.template_name, {'form': transactionsForm()})
    
    def post(self, request, id):
        form = transactionsForm(request.POST) 
        contact = form.data['contact']
        return redirect('/transaction/complete/'+id+'/'+contact+'/')  
