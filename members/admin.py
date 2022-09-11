from django.contrib import admin

from login.models import Admin
from . models import *
# Register your models here.
admin.site.register(Member)
admin.site.register(Admin)
