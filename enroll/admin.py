from django.contrib import admin
from enroll.models import testdb
# Register your models here.
@admin.register(testdb)
class testdbadmin(admin.ModelAdmin):
    list_display=["id","name","rollno","city"]