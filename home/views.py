from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render,HttpResponse

from .forms import dataadd, userform
from .models import user
from .models import signup


def index(request):
    if request.method == 'POST':
        stud=user.objects.all()
    else:
        stud=user.objects.all()
    return render(request,'index.html' ,{'form':stud})

def about(request):
    stud=user.objects.all()
    return render(request,'community.html' ,{'form':stud})

def contact(request):
    if request.method == 'POST':
        fm = dataadd(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your data has been Uploaded successfully!! You can Chheck it on our Community Page and Edit on our Edit page...')
        else:
            messages.info(request,'Not Saved!!!   Wrong Input')
        #return render(request,'contact.html' ,{'msg':a})
        return HttpResponseRedirect('/')
    else:
        fm = dataadd()
    return render(request,'contact.html' ,{'form':fm})

#def community(request):
 #   if request.method == 'POST':
  #      stud=user.objects.all()
   # else:
    #    stud=user.objects.all()
    #return render(request,'community.html' ,{'form':stud})

#def delete(request,id):
 #   if request.method=='POST':
  #      pi = user.objects.get(pk=id)
  #      pi.delete()
   #     return HttpResponseRedirect('/about')

def delete(request,id):
    pi = user.objects.get(pk=id)
    pi.delete()
    messages.success(request, 'Your data has been Deleted successfully!!')
    return HttpResponseRedirect('/about')

def update(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = dataadd(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request, 'Your data has been Updated successfully!!')
        return HttpResponseRedirect('/about')
    else:
        pi = user.objects.get(pk=id)
        fm = dataadd(instance=pi)
    return render(request,'update.html',{'form':fm})

def filter_n(request):
    if request.method=='POST':
        title = request.POST.get("n")
        flt=user.objects.filter(name__contains=title)
        return render(request,'filter.html',{'form':flt,'a':title})
    else:
        return HttpResponseRedirect('/')

def filter_e(request):
    if request.method=='POST':
        title = request.POST.get("e")
        flt=user.objects.filter(email__contains=title)
        return render(request,'filter.html',{'form':flt ,'a':title})
    else:
        return HttpResponseRedirect('/')

def filter_m(request):
    if request.method=='POST':
        title = request.POST.get("m")
        flt=user.objects.filter(mobile__contains=title)
        return render(request,'filter.html',{'form':flt})
    else:
        return HttpResponseRedirect('/')

def filter_i(request):
    if request.method=='POST':
        title = request.POST.get("i")
        flt=user.objects.filter(id__contains=title)
        return render(request,'filter.html',{'form':flt})
    else:
        return HttpResponseRedirect('/')

def login(request):
    if request.method=='POST':    
        dataz=userform(request.POST)
        if dataz.is_valid():
            user_instance = dataz.save(commit=False)
            em = user_instance.email
            pas = user_instance.password
            
            if signup.objects.filter(email=em):
                userone = signup.objects.filter(email=em)
                for i in userone:
                    usnm=i.Username
                    usps=i.password
                    usei=i.email
                if usps==pas:
                    
                    return render(request,'profile.html',{'usname':usnm,'usemail':usei})
                else:
                    return HttpResponse('password dost not match')
            else:
                return HttpResponse('Email is not valid')
        else:
            return HttpResponse('input is not valid')
    else:
        sf=userform()
        return render(request,'login.html',{'form':sf})

def sign_up(request):
    if request.method=='POST':    
        sf=userform(request.POST)
        if sf.is_valid():
            user_instance = sf.save(commit=False)
            user_instance.Username = user_instance.Username + '_careers360'
            user_instance.save()
        return HttpResponseRedirect('/login')
    else:
        sf=userform()
        return render(request,'signup.html',{'form':sf})

def profile(request):
    pass


def task(request):
    if request.method=='POST':    
        taskf=userform(request.POST)
        if taskf.is_valid():
            taskf.save()
        return render(request,'profile.html',{'form':taskf})
    else:
        taskf=userform()
        return render(request,'task.html',{'form':taskf})
    return render(request,'profile.html')




