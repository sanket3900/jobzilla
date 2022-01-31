from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(user)
admin.site.register(company)
admin.site.register(customer)
admin.site.register(company_gallary)
admin.site.register(customer_gallary)
admin.site.register(jobpost)
admin.site.register(postlike)
admin.site.register(companyfollowers)