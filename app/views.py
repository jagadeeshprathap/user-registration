from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_data(request):
    d={'to':Topicform(),'wo':Webpageform(),'ao':Accessrecordform()}
    
    if request.method=='POST':
        td=Topicform(request.POST)
        wd=Webpageform(request.POST)
        ad=Accessrecordform(request.POST)
        if td.is_valid() and wd.is_valid() and ad.is_valid():
            nstd=td.save(commit=False)
            nstd.save()

            nswd=wd.save(commit=False)
            nswd.topic_name=nstd
            nswd.save()

            nsad=ad.save(commit=False)
            nsad.name=nswd
            nsad.save()
            return HttpResponse('data inserted successfully completed')
        return HttpResponse('not valid')
            






    return render(request,'insert_data.html',d)