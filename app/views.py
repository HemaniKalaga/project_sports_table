from django.shortcuts import render
from app.models import *
# Create your views here.

def topic_data(request):

    QLTO=Topic.objects.all()   
    d={'data1':QLTO}
    return render(request,'topic_data.html',d)


def webpage_data(request):

    QLWO=Webpage.objects.all()
    d={'data2':QLWO}
    return render(request,'webpage_data.html',d)



def access_records_data(request):
    
    QLAO=AccessRecord.objects.all()
    d={'data3':QLAO}
    return render(request,'access_records_data.html',d)



