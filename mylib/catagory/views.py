from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

def Update(req,catagoryid):
    context = {}
    if(req.method=='GET'):
        cat=Catagory.objects.get(id=catagoryid)
        context['cat']=cat
        return render(req,'catagory/Update.html',context)
    else:
        Catagory.objects.filter(id=catagoryid).update(name=req.POST['category_name'])
        return HttpResponseRedirect('/')

def Delete(req, catagoryid):
     context = {}
     if (req.method == 'GET'):
            cat = Catagory.objects.get(id=catagoryid)
            context['cat'] = cat
            return render(req, 'catagory/Update.html', context)
        else:
            Catagory.objects.filter(id=catagoryid).Delete(name=req.POST['category_name'])
            return HttpResponseRedirect('/')
def List(req):
    context={}
    context['categories']=Catagory.objects.all()
    for cat in context['categories']:
        print(cat.name)

    return render(req,'catagory/index.html',context)

def Add(req):
    if(req.method=='GET'):
        return  render(req,'catagory/Add.html')
    else:
        data=req.POST
        print(data['catgoryname'])
        Catagory.objects.create(name=req.POST['category_name'])

        context={}
        context['message']='added is done'
        return render(req, 'catagory/Add.html',context)