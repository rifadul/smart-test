from django.shortcuts import render
from .models import DoctorInformation
# Create your views here.

def doctorInfo(request):
    doctorinfo = DoctorInformation.objects.all()
    return render(request,'doctor/doctor.html',{'doctorinfo':doctorinfo})


def doctorDetails(request,id):
    doctordetail = DoctorInformation.objects.get(id=id)
    return render(request,'doctor/doctorDetails.html',{'doctordetails':doctordetail})
