from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(siteList)
admin.site.register(Navbar)

# Brand Logo
admin.site.register(DonateBrandLogo)
admin.site.register(ITBrandLogo)
admin.site.register(CivilBrandLogo)
