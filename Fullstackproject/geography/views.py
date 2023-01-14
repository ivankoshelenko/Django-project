from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *

# Create your views here.
@login_required(login_url='signIn')
def geography(request):
    salaries = SalaryInCity.objects.all()
    cities =[]
    salaryArr =[]
    idArr =[]
    idcount =1
    for i in salaries:
        cities.append(i.city)
        salaryArr.append(i.salary)
        idArr.append(idcount)
        idcount+=1
    vacs =SalaryVacancies.objects.all()
    citiesArr =[]
    vacsArr =[]
    idVacArr =[]
    idVaccount =1
    for j in vacs:
        citiesArr.append(j.city)
        vacsArr.append(j.vacancies)
        idVacArr.append(idVaccount)
        idVaccount+=1
    img = Image.objects.all()
    imgArr = []
    for i in img:
        imgArr.append(i.image)
    return render(request,'geography.html',{'cities': cities,'salaries': salaryArr,'id' : idArr,'vCity':citiesArr,'vacancies':vacsArr,'vacId': idVacArr,'img':imgArr})