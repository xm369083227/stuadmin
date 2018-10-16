__author__ = 'Administrator'
from django.shortcuts import render,HttpResponse,redirect
from app01 import  models

def get_stu(request):
    stu_obj = models.Students.objects.all()
    cs_list = models.Classes.objects.all()
    return render(request, "get_stu.html",{"stu_obj":stu_obj,"cs_list":cs_list})
def add_stu(request):
    if request.method == "GET":
        return render(request, "get_stu.html")
    elif request.method == "POST":
        u = request.POST.get("username")
        a = request.POST.get("age")
        g = request.POST.get("gender")
        c = request.POST.get("cs")
        models.Students.objects.create(
            username = u,
            age = a,
            gender = g,
            cs_id = c,
        )
        return redirect("/get_stu/")