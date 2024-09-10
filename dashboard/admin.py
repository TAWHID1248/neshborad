from django.contrib import admin
from .models import PaymentGateway, Order, SalesResource, TrainingMaterial, Performance, Document

# Register your models here.
admin.site.register(PaymentGateway)
admin.site.register(Order)
admin.site.register(SalesResource)
admin.site.register(TrainingMaterial)
admin.site.register(Performance)
admin.site.register(Document)