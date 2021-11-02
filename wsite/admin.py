from django.contrib import admin

from wsite.models import WebsiteInfo, Package

admin.site.register(WebsiteInfo)
admin.site.register(Package)
