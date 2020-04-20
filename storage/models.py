from django.db import models

class admin(models.Model):
    # 项目号
    projectid=models.CharField(max_length=20,default='fengjie')
    # 编号
    itemNo=models.IntegerField(default=21)   # 使用数字长度设置无效
    # 类别
    type=models.CharField(max_length=300,default='m ')
    # 型号
    partNo = models.CharField(max_length=20)
    # 型号
    description = models.CharField(max_length=20)
    # 型号
    quantity = models.CharField(max_length=20)
    # 型号
    image = models.CharField(max_length=20)
    # 型号
    Vendor = models.CharField(max_length=20)
    # 型号
    period = models.CharField(max_length=20)
    # 型号
    cost = models.CharField(max_length=20)
    # 型号
    link = models.CharField(max_length=20)
    # 型号
    comment = models.CharField(max_length=20)
