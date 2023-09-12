from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *

# Create your views here.
class SecurityPage_SerializerViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = BannerITSerializer
    serializer_class1 = TechnologiesCategorySerializer
    serializer_class2 = OurServicesSerializer
    serializer_class3 = HomeTemplateSerializer
    serializer_class4 = ReadmoreSerializer
    serializer_class5 = SecurityPageSerializer

    serializer_class6 = ProductCategoryModelSerializer
    serializer_class7 = NoticeSerializer
    serializer_class8 = CompanySerializer
    serializer_class9 = BottomBannerSerializer
    serializer_class10 = TechnologySerializer
    

    def get(self, request):
        queryset = BannerIT.objects.filter(active=True).all()
        queryset1 = TechnologiesCategory.objects.filter(active=True).all()
        queryset2 = OurServices.objects.filter(active=True).all()
        queryset3 = HomeTemplate.objects.filter(active=True).all()
        queryset4 = Readmore.objects.filter(active=True).all()
        queryset5 = SecurityPage.objects.filter(active=True).all()

        queryset6 = ProductCategoryModel.objects.filter(active=True).all()
        queryset7 = NoticeModel.objects.filter(active=True).all()
        queryset8 = CompanyModel.objects.filter(active=True).all()
        queryset9 = BottomBanner.objects.filter(active=True).all()
        queryset10 = Technology.objects.filter(active=True).all()

        return Response({
                'BannerIT' :  self.serializer_class(queryset,many=True, context={'request':request}).data,
                'Technology' :  self.serializer_class10(queryset10,many=True).data,
                'TechnologiesCategory' :  self.serializer_class1(queryset1,many=True).data,
                'OurServices' :  self.serializer_class2(queryset2,many=True).data,
                'HomeTemplate' :  self.serializer_class3(queryset3,many=True, context={'request':request}).data,
                'Readmore' :  self.serializer_class4(queryset4,many=True, context={'request':request}).data,
                'SecurityPage' :  self.serializer_class5(queryset5,many=True).data,
                
                'Products' :  self.serializer_class6(queryset6,many=True, context={'request': request}).data,
                'Notice' :  self.serializer_class7(queryset7,many=True).data,
                'Company' :  self.serializer_class8(queryset8,many=True).data,
                'BottomBanner' :  self.serializer_class9(queryset9,many=True, context={'request':request}).data,
        })


# Contact Message Send

class Contact_ViewSet(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'type':'success','msg': 'Your message is safely stored in our database. We will reach you back.','status':status.HTTP_201_CREATED})
    



    
