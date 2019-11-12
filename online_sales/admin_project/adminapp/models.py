from django.db import models

class MerchantRegisteModel(models.Model):
    merchantid=models.IntegerField(primary_key=True,default=False)
    merchantname=models.CharField(max_length=30)
    contactno=models.IntegerField(max_length=10,unique=True)
    emailid=models.EmailField(unique=True)
    password=models.CharField(max_length=8)

class MerchantProductModel(models.Model):
    productid=models.IntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=30)
    price=models.FloatField()
    quantity=models.IntegerField()
    mid=models.ForeignKey(MerchantRegisteModel,on_delete=models.CASCADE,default=False)

