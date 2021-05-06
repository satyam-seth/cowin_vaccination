import requests
from django.shortcuts import render
from django.views import View
from datetime import date

# Create your views here.

def get_data(link):
    USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE="en-US,en;q=0.5"
    session=requests.Session()
    session.headers['User-Agent']=USER_AGENT
    session.headers['Accept-Language']=LANGUAGE
    session.headers['Content-Language']=LANGUAGE
    content=session.get(link)
    return content.json()

class StatesView(View):
    def get(self,request,*args,**kwargs):
        context=get_data('https://cdn-api.co-vin.in/api/v2/admin/location/states')
        return render(request,'core/states.html',context)

class DistrictsView(View):
    def get(self,request,state_id,*args,**kwargs):
        context=get_data(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}')
        return render(request,'core/districts.html',context)

class SessionsView(View):
    def get(self,request,district_id,*args,**kwargs):
        today_date=date.today().strftime("%d-%m-%Y")
        print(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={today_date}')
        context=get_data(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={today_date}')
        return render(request,'core/sessions.html',context)
