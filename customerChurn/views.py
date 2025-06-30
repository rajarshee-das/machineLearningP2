from django.shortcuts import render
from django.http import HttpResponse
import pickle
import os
from django.conf import settings

model_path=os.path.join(settings.BASE_DIR,"clf.pkl")

with open(model_path,"rb") as file:
    model=pickle.load(file)

def home(request):
    pred=None
    if request.method=="POST":
        a=int(request.POST['info1'])
        b=int(request.POST['info2'])
        c=int(request.POST['info3'])
        d=int(request.POST['info4'])

        e=int(request.POST['info5'])
        f=int(request.POST['info6'])
        g=int(request.POST['info7'])
        h=int(request.POST['info8'])

        i=int(request.POST['info9'])
        j=int(request.POST['info10'])
        k=int(request.POST['info11'])
        l=int(request.POST['info12'])

        m=int(request.POST['info13'])
        n=int(request.POST['info14'])
        o=int(request.POST['info15'])
        p=int(request.POST['info16'])

        q=int(request.POST['info17'])
        r=int(request.POST['info18'])
        s=int(request.POST['info19'])
        t=int(request.POST['info20'])
        situation=[[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]]
        pred=model.predict(situation)
    return render(request,"home.html",{"prediction":pred})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
