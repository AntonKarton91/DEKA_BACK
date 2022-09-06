from django.contrib import admin
from .models import TableColumns, Tasks

admin.site.register(TableColumns)
admin.site.register(Tasks)
# admin.site.register(CustomUser)