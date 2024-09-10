# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User

class PaymentGateway(models.Model):
    name = models.CharField(max_length=100)
    access_info = models.TextField()
    setup_guide_link = models.URLField()
    troubleshooting_guide = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)

class SalesResource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    link_to_tool = models.URLField()

class TrainingMaterial(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='training_materials/')
    material_type = models.CharField(max_length=20, choices=(('Video', 'Video'), ('PDF', 'PDF'), ('Document', 'Document')))


class Performance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kpi_name = models.CharField(max_length=100)
    value = models.IntegerField()
    target = models.IntegerField()


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
