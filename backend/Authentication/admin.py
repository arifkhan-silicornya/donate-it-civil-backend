from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','id','email','title','first_name','last_name','is_active','is_verified','is_superuser','is_staff']
    
admin.site.register(CodeVerification)

admin.site.register(PresentAddress) 
admin.site.register(PermanentAddress)
admin.site.register(CompanyDetail) 
admin.site.register(Contact_info)  
admin.site.register(SocialMediaLink) 
admin.site.register(EducationalQualification) 
