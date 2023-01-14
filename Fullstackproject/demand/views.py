
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def authcheck(request):
    return HttpResponse('Вы авторизованы')

def demand(request):
    jobs = AllJobsStats.objects.all()
    yearArr =[]
    avgSalArr =[]
    vacArr =[]
    for i in range(0,8):
        j =jobs[i]
        yearArr.append(j.year)
        avgSalArr.append(j.averageSalary)
        vacArr.append(j.vacanciesAmount)

    fullStackjobs = FullStackStats.objects.all()
    fYearArr =[]
    fAvgSalArr =[]
    fVacArr =[]
    for i in range(0,8):
        k =fullStackjobs[i]
        fYearArr.append(k.year)
        fAvgSalArr.append(k.averageSalary)
        fVacArr.append(k.vacanciesAmount)
    images = StatsImages.objects.all()
    return render(request,'demand.html',{'years':yearArr, 'avgSal':avgSalArr,'vacArr': vacArr, 'fYears' : fYearArr,'fSal': fAvgSalArr,
                                         'fVac':fVacArr,'images':StatsImages})
