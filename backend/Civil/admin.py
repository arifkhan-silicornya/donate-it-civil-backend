from django.contrib import admin
from .models import *
from .OrderModel import *
from .Payment_Model import *
# Register your models here.

admin.site.register(BannerCivil)
admin.site.register(FeatureWorksCategory)
admin.site.register(FeatureWorks)
admin.site.register(Architecture)
admin.site.register(DetailsOfFeatureDesign)
admin.site.register(ImagesOfDetailsDesign)
admin.site.register(OurServices)
admin.site.register(Readmore)
admin.site.register(SecurityPage)
admin.site.register(Contact)
admin.site.register(GlobalLocation)
admin.site.register(BottomBanner)


admin.site.register(ProductCategoryModel)
admin.site.register(ProductModel)
admin.site.register(NoticeModel)
admin.site.register(CompanyModel)


# Order Model
admin.site.register(OrderCivil) 
admin.site.register(DeliveryFileCivil) 
admin.site.register(OtherPdfCivil)  
admin.site.register(PersonalInfoCivil)  
admin.site.register(PresentAddressCivil) 
admin.site.register(PermanentAddressCivil)
admin.site.register(CompanyDetailCivil) 
admin.site.register(Contact_infoCivil)  
admin.site.register(SocialMediaLinkCivil)  


#payment
admin.site.register(PaymentMethod)  
admin.site.register(CompanyAccount)  
admin.site.register(TransactionModelCivil)  