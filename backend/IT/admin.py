from django.contrib import admin
from .models import *
from .OrderModel import *
# Register your models here.

admin.site.register(BannerIT)
admin.site.register(TechnologiesCategory)
admin.site.register(Technology)
admin.site.register(OurServices)
admin.site.register(HomeTemplate)
admin.site.register(Readmore)
admin.site.register(SecurityPage)
admin.site.register(Contact)

admin.site.register(ProductModel)
admin.site.register(NoticeModel)
admin.site.register(CompanyModel)
admin.site.register(ProductCategoryModel)

# Order Model
admin.site.register(OrderIt) 
admin.site.register(OtherPdfIT)  
admin.site.register(PersonalInfoIT)  
admin.site.register(PresentAddressIT) 
admin.site.register(PermanentAddressIT)
admin.site.register(CompanyDetailIT) 
admin.site.register(Contact_infoIT)  
admin.site.register(SocialMediaLinkIT)  
