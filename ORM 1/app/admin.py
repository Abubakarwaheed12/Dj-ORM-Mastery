from django.contrib import admin
from app.models import Students ,Teacher
# Register your models here.


@admin.register(Students)
class StuAdmin(admin.ModelAdmin):
    list_display=['id' , 'name', 'age' ,]
    
    
@admin.register(Teacher)
class StuAdmin(admin.ModelAdmin):
    list_display=['id' , 'name', 'qualification' ]