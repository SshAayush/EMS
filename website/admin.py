from django.contrib import admin
from .models import UsersList
from .models import Staff
from .models import Time

# Register your models here.
admin.site.register(UsersList)
admin.site.register(Staff)
admin.site.register(Time)