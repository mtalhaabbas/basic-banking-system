from django.contrib import admin
from .models import *


class customerAdmin(admin.ModelAdmin):
    model = customer
    list_display = ['account_type','account_number','full_name','email','address','current_balance']
admin.site.register(customer,customerAdmin)

class transcationAdmin(admin.ModelAdmin):
    model = transcation
    list_display = ['user','date','time','description','dr','cr','balance']
admin.site.register(transcation,transcationAdmin)
