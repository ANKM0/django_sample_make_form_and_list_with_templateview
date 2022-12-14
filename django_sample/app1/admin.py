from django.contrib import admin
from .models import TestData


@admin.register(TestData)
class ProductDataAdmin(admin.ModelAdmin):
    model = TestData
    list_display = ["number", "name", "price"]
    ordering = ["number"]
