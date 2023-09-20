from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *

# Create your views here.
class Civil_Page_ViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = BannerCivilSerializer
    serializer_class1 = FeatureWorksCategoryerializer
    serializer_class2 = OurServicesSerializer
    serializer_class3 = ArchitectureSerializer
    serializer_class4 = ReadmoreSerializer
    serializer_class5 = SecurityPageSerializer

    serializer_class6 = ProductCategoryModelSerializer
    serializer_class7 = NoticeSerializer
    serializer_class8 = CompanySerializer 
    serializer_class9 = BottomBannerSerializer

    def get(self, request):
        queryset = BannerCivil.objects.filter(active=True).all()
        queryset1 = FeatureWorksCategory.objects.filter(active=True).all()
        queryset2 = OurServices.objects.filter(active=True).all()
        queryset3 = Architecture.objects.filter(active=True).all()
        queryset4 = Readmore.objects.filter(active=True).all()
        queryset5 = SecurityPage.objects.filter(active=True).all()

        queryset6 = ProductCategoryModel.objects.filter(active=True).all()
        queryset7 = NoticeModel.objects.filter(active=True).all()
        queryset8 = CompanyModel.objects.filter(active=True).all()
        queryset9 = BottomBanner.objects.filter(active=True).all()

        return Response({
                'BannerIT' :  self.serializer_class(queryset,many=True).data,
                'TechnologiesCategory' :  self.serializer_class1(queryset1,many=True).data,
                'OurServices' :  self.serializer_class2(queryset2,many=True).data,
                'atchitecture_OR_featureDesign' :  self.serializer_class3(queryset3,many=True).data,
                'Readmore' :  self.serializer_class4(queryset4,many=True).data,
                'SecurityPage' :  self.serializer_class5(queryset5,many=True).data,
                
                'Product' :  self.serializer_class6(queryset6,many=True).data,
                'Notice' :  self.serializer_class7(queryset7,many=True).data,
                'Company' :  self.serializer_class8(queryset8,many=True).data,
                'BottomBanner' :  self.serializer_class9(queryset9,many=True).data[0]
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


class ProductViewIT(APIView): 
    permission_classes = (AllowAny,)
    def get_product(self, pk):
        try:
            return ProductModel.objects.filter(id=pk)
        except:
            return Response({'type': 'error', 'message': 'Product not found'})
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_product(pk)
            serializer = ProductSerializer(instance, many=True, context={'request':request})
        else:
            instance = ProductModel.objects.filter(active=True).all()
            serializer = ProductSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class ServicesLinkList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = OurServices.objects.filter(active=True).all()
    serializer_class = OurServicesSerializer


class DetailsDesignView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = DetailsOfFeatureDesign.objects.filter(active=True).all()
    serializer_class = DetailsOfFeatureDesignSerializer

    def get(self, request, pk):
        try:
            id = pk
        except:
            return Response({'type': 'error','message': 'id not found'})
        if Architecture.objects.filter(id=id).exists():
            instance = Architecture.objects.get(id=id)
            if DetailsOfFeatureDesign.objects.filter(Architecture=instance , active=True).exists():
                obj = DetailsOfFeatureDesign.objects.get(Architecture=instance , active=True)
                serializer = self.serializer_class(obj, many=False, context={'request':request}).data
                return Response(serializer, status=status.HTTP_200_OK)
            else:
                return Response({'type': 'error','message': 'id not exist'})
        else:
            return Response({'type': 'error','message': 'id not exist'})

