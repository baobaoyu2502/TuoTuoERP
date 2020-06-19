import decimal
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import json
from django.core.paginator import Paginator
import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    #request.POST
    #request.GET
    return render(request,"index.html")

def stockList(request):
    #request.POST
    #request.GET
    return render(request, "stockList.html")

def orderList(request):
    #request.POST
    #request.GET
    return render(request, "orderList.html")

def base(request):
    #request.POST
    #request.GET
    return render(request,"base.html")

def stockOut(request):
    #request.POST
    #request.GET
    return render(request, "stockOut.html")

def stockIn(request):
    #request.POST
    #request.GET
    return render(request, "stockIn.html")

def test(request):
    #request.POST
    #request.GET
    data = admin.objects.all()
    content = {'data': data}
    return render(request,"test.html",content)

def stocklistview(request):
    dates = admin.objects.all()  # 自行创建测试数据。
    dataCount = dates.count()  # 数据总数
    lis = []
    for i in dates:
        dict = {}
        dict['id'] = i.id  # 与前端一一对应，自行设置要展示的字段
        dict['projectid'] = i.projectid  # 外键字段
        dict['itemNo'] = i.itemNo  # 外键字段
        dict['type'] = i.type
        dict['partNo'] = i.partNo
        dict['description'] = i.description
        dict['quantity'] = i.quantity
        dict['image'] = i.image  # 外键字段
        dict['Vendor'] = i.Vendor  # 外键字段
        dict['period'] = i.period
        dict['cost'] = i.cost
        dict['link'] = i.link
        dict['comment'] = i.comment
        lis.append(dict)
    pageIndex = request.GET.get('page') #前台传的值，
    pageSize = request.GET.get('limit') #前台传的值
    pageInator = Paginator(lis, pageSize)#导入分页模块分页操作，不写前端只展示一页数据，
    contacts = pageInator.page(pageIndex)#导入分页模块分页操作，不写前端只展示一页数据，
    res = []
    for i in contacts:
        res.append(i)
    print(res)
    Result = {"code": 0, "msg": "", "count": dataCount, "data": res}
    # json.dumps(Result, cls=DateEncoder)没有时间字段问题可直接返回此代码。有就返回下面代码
    return HttpResponse(json.dumps(Result, cls=DecimalEncoder), content_type="application/json")

#解决时间字段json问题
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)

class DecimalEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, decimal.Decimal):
            return float(o)

        super(DecimalEncoder, self).default(o)





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
    return render(request,'stockList.html', content)

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