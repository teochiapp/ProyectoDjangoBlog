from django.contrib import admin
from .models import Page

# Register your models here.

admin.site.register(Page)

title = "Proyecto con Python"
subtitle = "Panel de gestión"

#Config del panel

admin.site.site_title = title
admin.site.site_header = subtitle
admin.site.index_title = subtitle