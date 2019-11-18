from django.db.models import Max
from django.shortcuts import render
from .models import Marks


def cover(request):
    return render(request,'cover.html')

def index(request):
    return render(request,'main.html')

def organisars(request):
    return render(request, 'leader1.html')

def contstant(request):
    return render(request, 'contstant.html')

def staff(request):
    return render(request, 'staff.html')

def progress(request):
    return render(request, 'timer.html' )

def marks(request):
    all_mark = Marks.objects.all()
    return render(request, 'marks.html', {'All_mark':all_mark})

def ranks(request):
    first = Marks.objects.all()
    return render(request, 'ranks.html', {'First':first})

def getmarks(request):
    DEPT_SEC = request.POST["DEPT_SEC"]
    NAME = request.POST["NAME"]
    PRESENTATION = request.POST["PRESENTATION"]
    QUERIES = request.POST["QUERIES"]
    COMMUNICATION = request.POST["COMMUNICATION"]
    AUDIENCE = request.POST["AUDIENCE"]
    TOTAL = request.POST["TOTAL"]

    marks = Marks(DEPT_SEC=DEPT_SEC, NAME=NAME, PRESENTATION=PRESENTATION, QUERIES=QUERIES, COMMUNICATION=COMMUNICATION, AUDIENCE=AUDIENCE, TOTAL=TOTAL )
    marks.save()
    all_mark = Marks.objects.all()
    return render(request, 'marks.html', {'All_mark': all_mark})
    # first = Marks.objects.all().aggregate(Max('TOTAL'))
    # return render(request, 'ranks.html', {'First':first})


