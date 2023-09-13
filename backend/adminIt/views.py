from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.models import *
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,  UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin)

# Create your views here.
class BannerView(APIView):
    permission_classes = (AllowAny,)
    def get_banner(self, pk):
            return BannerIT.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_banner(pk)
            serializer = BannerITSerializer(instance, context={'request':request})
        else:
            instance = BannerIT.objects.all()
            serializer = BannerITSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = BannerITSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = BannerIT.objects.get(id=pk)    
        except BannerIT.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BannerITSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_banner(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TechnologiesCategoryView(APIView):
    permission_classes = (AllowAny,)
    def get_technologies_category(self, pk):
            return TechnologiesCategory.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_technologies_category(pk)
            serializer = TechnologiesCategorySerializer(instance, many=True, context={'request':request})
        else:
            instance = TechnologiesCategory.objects.all()
            serializer = TechnologiesCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = TechnologiesCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = TechnologiesCategory.objects.get(id=pk)    
        except TechnologiesCategory.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = TechnologiesCategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_technologies_category(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TechnologyView(APIView):
    permission_classes = (AllowAny,)
    def get_technology(self, pk):
        try:
            return Technology.objects.filter(id=pk)
        except:
            return Response({'type': 'error', 'message': 'Technology not found'})
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_technology(pk)
            serializer = TechnologySerializer(instance, many=True, context={'request':request})
        else:
            instance = Technology.objects.all()
            serializer = TechnologySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = TechnologySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Technology.objects.get(id=pk)    
        except Technology.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = TechnologySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_technology(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

class NoticeView(APIView):
    permission_classes = (AllowAny,)
    def get_notice(self, pk):
            return NoticeModel.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_notice(pk)
            serializer = NoticeSerializer(instance, many=True, context={'request':request})
        else:
            instance = NoticeModel.objects.all()
            serializer = NoticeSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = NoticeModel.objects.get(id=pk)    
        except NoticeModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = NoticeSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_notice(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
class SecurityView(APIView):
    permission_classes = (AllowAny,)
    def get_security(self, pk):
            return SecurityPage.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_security(pk)
            serializer = SecurityPageSerializer(instance, many=True, context={'request':request})
        else:
            instance = SecurityPage.objects.all()
            serializer = SecurityPageSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = SecurityPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = SecurityPage.objects.get(id=pk)    
        except SecurityPage.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = SecurityPageSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_security(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

class ContactView(APIView):
    permission_classes = (AllowAny,)
    def get_contact(self, pk):
            return Contact.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_contact(pk)
            serializer = ContactSerializer(instance, many=True, context={'request':request})
        else:
            instance = Contact.objects.all()
            serializer = ContactSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Contact.objects.get(id=pk)    
        except Contact.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_contact(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
    
class CompanyView(APIView):
    permission_classes = (AllowAny,)
    def get_company(self, pk):
            return CompanyModel.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_company(pk)
            serializer = CompanySerializer(instance, many=True, context={'request':request})
        else:
            instance = CompanyModel.objects.all()
            serializer = CompanySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = CompanyModel.objects.get(id=pk)    
        except CompanyModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_company(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class OurServicesView(APIView):
    permission_classes = (AllowAny,)
    def get_service(self, pk):
            return OurServices.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_service(pk)
            serializer = OurServicesSerializer(instance, many=True, context={'request':request})
        else:
            instance = OurServices.objects.all()
            serializer = OurServicesSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = OurServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = OurServices.objects.get(id=pk)    
        except OurServices.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = OurServicesSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_service(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ReadmoreView(APIView):
    permission_classes = (AllowAny,)
    def get_readmore(self, pk):
            return Readmore.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_readmore(pk)
            serializer = ReadmoreSerializer(instance, many=True, context={'request':request})
        else:
            instance = Readmore.objects.all()
            serializer = ReadmoreSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = ReadmoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Readmore.objects.get(id=pk)    
        except Readmore.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ReadmoreSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_readmore(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HomeView(APIView):
    permission_classes = (AllowAny,)
    def get_home(self, pk):
            return HomeTemplate.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_home(pk)
            serializer = HomeTemplateSerializer(instance, many=True, context={'request':request})
        else:
            instance = HomeTemplate.objects.all()
            serializer = HomeTemplateSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = HomeTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = HomeTemplate.objects.get(id=pk)    
        except HomeTemplate.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = HomeTemplateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_home(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CategoryView(APIView):
    permission_classes = (AllowAny,)
    def get_category(self, pk):
            return ProductCategoryModel.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_category(pk)
            serializer = CategorySerializer(instance, many=True, context={'request':request})
        else:
            instance = ProductCategoryModel.objects.all()
            serializer = CategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = ProductCategoryModel.objects.get(id=pk)    
        except ProductCategoryModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_category(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ProductView(APIView):
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
            instance = ProductModel.objects.all()
            serializer = ProductSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = ProductModel.objects.get(id=pk)    
        except ProductModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_product(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderITView(APIView):
    permission_classes = (AllowAny,)
    def get_orderIt(self, pk):
            return OrderIt.objects.filter(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_orderIt(pk)
            serializer = OrderItSerializer(instance, many=True, context={'request':request})
        else:
            instance = OrderIt.objects.all()
            serializer = OrderItSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        try:
            userId = request.data['user']
        except:
            return Response({'type': 'error', 'message': 'User not found'})
        
        if User.objects.filter(id=userId).exists():
            user = User.objects.get(id=userId)
        else:
            return Response({"type":"error","msg":"User not found"})  
        serializer = OrderItSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = OrderIt.objects.get(id=pk)    
        except OrderIt.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = OrderItSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated Banner")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_orderIt(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderPdfView(GenericAPIView):
    permission_classes = (AllowAny,)
    queryset = OrderPdfIT.objects.all()
    serializer_class = OrderPdfSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        if pk is not None:
            # Retrieve a single item
            instance = self.get_object()
            serializer = self.serializer_class(instance)
        else:
            # List all items
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            orderId = request.data['orderit']
        except:
            return Response({'type': 'error', 'message': 'User not found'})
        
        if OrderIt.objects.filter(id=orderId).exists():
            order = OrderIt.objects.get(id=orderId)
        else:
            return Response({"type":"error","msg":"Order not found"}) 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(orderit=order)
        else:
            return Response({"type":"error","message":"Order not found"})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class OtherPdfListCreateView(GenericAPIView, ListModelMixin, 
                   CreateModelMixin):
    permission_classes = (AllowAny,)
    queryset = OtherPdfIT.objects.all()
    serializer_class = OtherPdfSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class OtherPdfRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, 
                   UpdateModelMixin, DestroyModelMixin):
    permission_classes = (AllowAny,)
    queryset = OtherPdfIT.objects.all()
    serializer_class = OtherPdfSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class PersonalInfoListCreateView(ListCreateAPIView):
    queryset = PersonalInfoIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PersonalInfoSerializer
    
    
class PersonalInfoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfoIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PersonalInfoSerializer
    
class PresentAddressListCreateView(ListCreateAPIView):
    queryset = PresentAddressIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PresentAddressSerializer
    
class PresentAddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PresentAddressIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PresentAddressSerializer
    

class PermanentAddressListCreateView(ListCreateAPIView):
    queryset = PermanentAddressIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PermanentAddressSerializer
    
class PermanentAddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PermanentAddressIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PermanentAddressSerializer
    
    
class CompanyDetailListCreateView(ListCreateAPIView):
    queryset = CompanyDetailIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CompanyDetailSerializer
    
class CompanyDetailRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyDetailIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CompanyDetailSerializer
    
    
class Contact_infoListCreateView(ListCreateAPIView):
    queryset = Contact_infoIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = Contact_infoSerializer
    
class Contact_infoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contact_infoIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = Contact_infoSerializer
    

class SocialMediaLinkListCreateView(ListCreateAPIView):
    queryset = SocialMediaLinkIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SocialMediaLinkSerializer
    
class SocialMediaLinkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SocialMediaLinkIT.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SocialMediaLinkSerializer
    
    
# ----------------------------header views---------------------------

class siteListCreateView(ListCreateAPIView):
    queryset = siteList.objects.all()
    permission_classes = [AllowAny]
    serializer_class = siteListSerializer

class siteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = siteList.objects.all()
    permission_classes = [AllowAny]
    serializer_class = siteListSerializer
    
    
class NavbarCreateView(ListCreateAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NavbarSerializer

class NavbarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NavbarSerializer
    
    
# ------------------------footer views-------------------------

class footerSectionListCreateView(ListCreateAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerSectionSerializer
    
class footerSectionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerSectionSerializer
    
class footerItemListCreateView(ListCreateAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerItemSerializer
    
class footerItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerItemSerializer
    
    
class footerHeadOfficeListCreateView(ListCreateAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerHeadOfficeSerializer
    
class footerHeadOfficeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerHeadOfficeSerializer
    

class footerSocialIconListCreateView(ListCreateAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerSocialIconSerializer
    
class footerSocialIconRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerSocialIconSerializer
    
class PaymentIconListCreateView(ListCreateAPIView):
    queryset = PaymentIcon.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PaymentIconSerializer
    
class PaymentIconRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentIcon.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PaymentIconSerializer
    
    
class NewsLetterListCreateView(ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NewsLetterSerializer
    
class NewsLetterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = NewsLetter.objects.all()
    permission_classes = [AllowAny]
    serializer_class = NewsLetterSerializer
    

                         