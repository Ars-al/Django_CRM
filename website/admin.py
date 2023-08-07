from django.contrib import admin
from .models import Record, HrRecord, EmployeeRecord


admin.site.register(Record)
admin.site.register(HrRecord)
admin.site.register(EmployeeRecord)