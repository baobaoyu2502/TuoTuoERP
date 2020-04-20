from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    #request.POST
    #request.GET
    return render(request,"index.html")

def base(request):
    #request.POST
    #request.GET
    return render(request,"base.html")

def add(request):
    #request.POST
    #request.GET
    return render(request,"add.html")

def test(request):
    #request.POST
    #request.GET
    return render(request,"test.html")

def all_page(request):

    data = admin.objects.all()
    content={'data': data}
    return render(request, 'all.html', content)




# 2.增
@csrf_exempt
def add_storage(request):
    productid = request.POST['productid']
    itemNo = request.POST['itemNo']
    image = request.FILES['description']
    fname = os.path.join(settings.MEDIA_ROOT, image.name)
    with open(fname, 'wb') as pic:
        for c in image.chunks():
            pic.write(c)

    admin=admin()
    admin.productid=productid
    admin.itmeNo=itmeNo
    # 存访问路径到数据库
    admin.image = os.path.join("/static/media/", image.name)
    admin.save()

    return redirect('/all')

# 3.1.查 - name
def search_item(request):
    itemNo = request.GET['q']
    itemNo=admin.objects.filter(itemNo=itemNo)
    content={'data':itemNo}
    return render(request,'all.html', content)

# 3.2.查 - id
def search_student_id(request,student_id):
    student=admin.objects.filter(id=student_id)
    content = {'data': student}
    print(content)
    return  render(request,'student/update.html',content)

# 4.改
@csrf_exempt
def update_student(request):

    id=request.POST['t_id']
    t_name = request.POST['tName']
    t_age = request.POST['tAge']
    # 缺陷：文件必传
    t_image = request.FILES['tImage']

    fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
    with open(fname, 'wb') as pic:
        for c in t_image.chunks():
            pic.write(c)
    t_image = os.path.join("/static/media/", t_image.name)

    admin.objects.filter(id=id).update(t_name=t_name,t_age=t_age,t_image=t_image)
    return redirect('/allPage')

# 5.删
def delete_student(request,itemNo):
    admin.objects.filter(id=itemNo).delete()
    return redirect('/all')