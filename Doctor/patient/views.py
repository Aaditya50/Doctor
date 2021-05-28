from django.shortcuts import render , HttpResponseRedirect
from .form import Patientinfo 
from .models import User

# This will show and add data .
def add_show(request):
    if request.method == 'POST':
        fm = Patientinfo(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            no = fm.cleaned_data['contact']
            ct = fm.cleaned_data['city']
            reg = User(name=nm,contact=no,city=ct) 
            reg.save()
            fm = Patientinfo()

    else:
        fm = Patientinfo()
    doc = User.objects.all()
    return render(request,'patient/addshow.html',{'form':fm , 'doct':doc})

#This will update patients data 
def update(request ,id):
    if request.method =='POST':
        pt = User.objects.get(pk=id)
        fm = Patientinfo(request.POST , instance=pt)
        if fm.is_valid():
            fm.save()
    else:
            pt=User.objects.get(pk=id)
            fm = Patientinfo(instance=pt)
    return render(request , 'patient/updatepatient.html' , {'form':fm} )

#This will delete data
def delete(request , id):
    if request.method == 'POST':
        pt=User.objects.get(pk=id)
        pt.delete()
        return HttpResponseRedirect('/')