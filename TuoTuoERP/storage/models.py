from django.db import models

class admin(models.Model):
    # 项目号
    projectid=models.CharField(max_length=20,default='tuotuo')
    # 编号
    itemNo=models.CharField(max_length=20)   # 使用数字长度设置无效
    # 类别
    type=models.CharField(max_length=300,default='m ')
    # 型号
    partNo = models.CharField(max_length=20)
    # 描述
    description = models.CharField(max_length=20)
    # 数量
    quantity = models.CharField(max_length=20)
    # 示意图
    image = models.CharField(max_length=20)
    # 供应商
    Vendor = models.CharField(max_length=20)
    # 货期
    period = models.CharField(max_length=20)
    # 成本
    cost = models.CharField(max_length=20)
    # 链接
    link = models.CharField(max_length=20)
    # 备注
    comment = models.CharField(max_length=20)


class stockHis(models.Model):
    # 项目号
    projectid = models.CharField(max_length=20, default='tuotuo')
    # 编号
    itemNo = models.CharField(max_length=20)  # 使用数字长度设置无效
    # 类别
    type = models.CharField(max_length=300, default='m ')
    # 型号
    partNo = models.CharField(max_length=20)
    # 描述
    description = models.CharField(max_length=20)
    # 数量
    quantity = models.CharField(max_length=20)
    # 示意图
    image = models.CharField(max_length=20)
    # 供应商
    Vendor = models.CharField(max_length=20)
    # 货期
    period = models.CharField(max_length=20)
    # 成本
    cost = models.CharField(max_length=20)
    # 链接
    link = models.CharField(max_length=20)
    # 备注
    comment = models.CharField(max_length=20)


class projectAdmin(models.Model):
    # 项目号
    projectid = models.CharField(max_length=20, default='tuotuo')
    # 编号
    itemNo = models.CharField(max_length=20)  # 使用数字长度设置无效
    # 类别
    type = models.CharField(max_length=300, default='m ')
    # 型号
    partNo = models.CharField(max_length=20)
    # 描述
    description = models.CharField(max_length=20)
    # 需求数量
    quantity = models.CharField(max_length=20)


class orderAdmin(models.Model):
    # 项目号
    projectid = models.CharField(max_length=20, default='tuotuo')
    # 编号
    itemNo = models.CharField(max_length=20)  # 使用数字长度设置无效
    # 类别
    type = models.CharField(max_length=300, default='m ')
    # 型号
    partNo = models.CharField(max_length=20)
    # 描述
    description = models.CharField(max_length=20)
    # 需求数量
    quantity = models.CharField(max_length=20)