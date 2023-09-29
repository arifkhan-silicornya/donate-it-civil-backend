from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination
from IT.models import *
from IT.Paymentserializers import *   
from IT.Payment_Model import *
from Authentication.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView ,UpdateAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,  UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin)

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10
    
class BannerView(APIView):
    permission_classes = (IsAdminUser,)
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
            return Response({"type": "success", "msg": "Banner created successfully"})
        return Response({"type": "error", "msg": "Banner creation failed"})

    def patch(self, request, pk):
        try:
            instance = BannerIT.objects.get(id=pk)    
        except BannerIT.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BannerITSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Banner successfully updated"})
        return Response({"type": "error", "msg": "Banner updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_banner(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BottomBannerView(APIView):
    permission_classes = (IsAdminUser,)
    def get_banner(self, pk):
            return BottomBanner.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_banner(pk)
            serializer = BottomBannerSerializer(instance, context={'request':request})
        else:
            instance = BottomBanner.objects.all()
            serializer = BottomBannerSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = BottomBannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Banner created successfully"})
        return Response({"type": "error", "msg": "Banner creation failed"})

    def patch(self, request, pk):
        try:
            instance = BottomBanner.objects.get(id=pk)    
        except BottomBanner.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BottomBannerSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Banner successfully updated"})
        return Response({"type": "error", "msg": "Banner updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_banner(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TechnologiesCategoryAPIView(APIView):
    permission_classes = (IsAdminUser,)
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
    def post(self, request):
        serializer = TechnologiesCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Technology category successfully created"})
        return Response({"type": "error", "msg": "Technology category creation failed"})

    def patch(self, request, pk):
        try:
            instance = TechnologiesCategory.objects.get(id=pk)    
        except TechnologiesCategory.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = TechnologiesCategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Technology category successfully updated"})
        return Response({"type": "error", "msg": "Technology category updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_technologies_category(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Technology category successfully deleted"})

class TechnologyView(APIView):
    permission_classes = (IsAdminUser,)
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
        ctg = request.data['category']
        ctg_model = TechnologiesCategory.objects.filter(category=ctg).first()
        serializer = TechnologySerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(category=ctg_model)
            return Response({"type": "success", "msg": "Technology successfully created"})
        return Response({"type": "success", "msg": "Technology creation failed"})

    def patch(self, request, pk):
        try:
            instance = Technology.objects.get(id=pk)    
            ctg = request.data['category']
        except Technology.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if TechnologiesCategory.objects.filter(id=ctg).exists():
            ctg_model = TechnologiesCategory.objects.get(id=ctg)
            serializer = TechnologySerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(category=ctg_model)
                return Response({"type": "success", "msg": "Technology successfully updated"})
        return Response({"type": "error", "msg": "Technology updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_technology(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Technology successfully deleted"})    
    
class TechnologyStatusChange(APIView):
    permission_classes = (IsAdminUser,)
    def patch(self, request, pk):
        try:
            instance = Technology.objects.get(id=pk)    
            serializer = TechnologySerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"type": "success", "msg": "Technology successfully updated!"})
            return Response({"type": "error", "msg": "Technology updation failed!"})
        except Technology.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

class NoticeView(APIView):
    permission_classes = (IsAdminUser,)
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
        serializer = NoticeSerializer(data=request.data or request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Notice created successfully"})
        return Response({"type": "error", "msg": "Notice creation failed"})

    def patch(self, request, pk):
        try:
            instance = NoticeModel.objects.get(id=pk)    
        except NoticeModel.DoesNotExist:
            return Response({"type": "error", "msg": "Notice objects not found"})
        serializer = NoticeSerializer(instance, data=request.data or request.FILES, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Notice Updated successfully"})
        return Response({"type": "error", "msg": "Notice updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_notice(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Notice deleted successfully"})  
    
class SecurityView(APIView):
    permission_classes = (IsAdminUser,)
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
            return Response({"type": "success", "msg": "Security created successfully"})
        return Response({"type": "error", "msg": "Security creation failed"})

    def patch(self, request, pk):
        try:
            instance = SecurityPage.objects.get(id=pk)    
        except SecurityPage.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = SecurityPageSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Security udated successfully"})
        return Response({"type": "error", "msg": "Security updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_security(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Security deleted successfully"}) 
    

class ContactView(APIView):
    permission_classes = (IsAdminUser,)
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
    permission_classes = (IsAdminUser,)
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
            return Response({"type": "success", "msg": "Company created successfully"})
        return Response({"type": "error", "msg": "Company creation failed"})

    def patch(self, request, pk):
        try:
            instance = CompanyModel.objects.get(id=pk)    
        except CompanyModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Company updated successfully"})
        return Response({"type": "error", "msg": "Company updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_company(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Company deleted successfully"}) 
    
class OurServicesView(APIView):
    permission_classes = (IsAdminUser,)
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
        serializer = OurServicesSerializer(data=request.data or request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Service created successfully"})
        return Response({"type": "error", "msg": "Service creation failed"})

    def patch(self, request, pk):
        try:
            instance = OurServices.objects.get(id=pk)    
        except OurServices.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = OurServicesSerializer(instance, data=request.data or request.FILES, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Service updated successfully"})
        return Response({"type": "error", "msg": "Service updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_service(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Service deleted successfully"})
    
    
class ReadmoreView(APIView):
    permission_classes = (IsAdminUser,)
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
            return Response({"type": "success", "msg": "Readmore created successfully"})
        return Response({"type": "error", "msg": "Readmore creation failed"})

    def patch(self, request, pk):
        try:
            instance = Readmore.objects.get(id=pk)    
        except Readmore.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ReadmoreSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Readmore updated successfully"})
        return Response({"type": "error", "msg": "Readmore updation failed"})
    
    def delete(self, request, pk):
        instance = self.get_readmore(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HomeTemplateView(APIView):
    permission_classes = (IsAdminUser,)
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
            return Response({"type":"success","msg":"Template successfully created!"})
        return Response({"type":"error","msg":"Template creation failed!"})

    def patch(self, request, pk):
        try:
            instance = HomeTemplate.objects.get(id=pk)    
        except HomeTemplate.DoesNotExist:
            return Response({"type":"error", "msg":"Template doesn't exist!"})
        serializer = HomeTemplateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success", "msg":"Template successfully updated!"})
        return Response({"type":"error", "msg":"Template updation failed!"})
    
    def delete(self, request, pk):
        instance = self.get_home(pk)
        instance.delete()
        return Response({"type":"success","msg":"Template successfully deleted!"})
    
    
class CategoryView(APIView):
    permission_classes = (IsAdminUser,)
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
            return Response({"type": "success", "msg": "Category successfully created!"})
        return Response({"type": "error", "msg": "Category creation failed!"})

    def patch(self, request, pk):
        try:
            instance = ProductCategoryModel.objects.get(id=pk)    
        except ProductCategoryModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Category successfully updated!"})
        return Response({"type": "error", "msg": "Category  updation failed!"})
    
    def delete(self, request, pk):
        instance = self.get_category(pk)
        instance.delete()
        return Response({"type": "success", "msg": "Successfully deleted"})
    
    
class ProductView(APIView):
    permission_classes = (IsAdminUser,)
    def get_product(self, pk):
        try:
            return ProductModel.objects.filter(id=pk)
        except:
            return Response({'type': 'error', 'msg': 'Product not found'})
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_product(pk)
            serializer = ProductSerializer(instance, many=True, context={'request':request})
        else:
            instance = ProductModel.objects.all()
            serializer = ProductSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        ctg = request.data['category']
        ctg_model = ProductCategoryModel.objects.filter(category=ctg).first()
        serializer = ProductSerializer(data=request.data or request.FILES, partial=True)
        if serializer.is_valid():
            serializer.save(category=ctg_model)
            return Response({'type': 'success', 'msg': 'Product created successfully'})
        return Response({'type': 'error', 'msg': 'Product creation failed'})

    def patch(self, request, pk):
        try:
            instance = ProductModel.objects.get(id=pk)    
        except ProductModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        ctg = request.data['category']
        if ProductCategoryModel.objects.filter(id=ctg).exists():
            ctg_model = ProductCategoryModel.objects.get(id=ctg)
            serializer = ProductSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(category=ctg_model)
                return Response({'type': 'success', 'msg': 'Product successfully updated'})
        else:
            return Response({'type': 'error', 'msg': 'Product category not exist'})
    
    def delete(self, request, pk):
        instance = self.get_product(pk)
        instance.delete()
        return Response({'type': 'success', 'msg': 'Product deleted successfully'})
    
class ProductStatusChange(APIView):
    permission_classes = (IsAdminUser,)
    def patch(self, request, pk):
        try:
            instance = ProductModel.objects.get(id=pk)    
            serializer = ProductSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"type": "success", "msg": "Product successfully updated!"})
            return Response({"type": "error", "msg": "Product updation failed!"})
        except ProductModel.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        
class OrderITView(APIView):
    permission_classes = (IsAdminUser,)
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
    permission_classes = (IsAdminUser,)
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
    


class OtherPdfListCreateView(GenericAPIView, ListModelMixin, 
                   CreateModelMixin):
    permission_classes = (IsAdminUser,)
    queryset = OtherPdfIT.objects.all()
    serializer_class = OtherPdfSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class OtherPdfRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, 
                   UpdateModelMixin, DestroyModelMixin):
    permission_classes = (IsAdminUser,)
    queryset = OtherPdfIT.objects.all()
    serializer_class = OtherPdfSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class PersonalInfoListCreateView(ListCreateAPIView):
    queryset = PersonalInfoIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PersonalInfoSerializer
    
    
class PersonalInfoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PersonalInfoIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PersonalInfoSerializer
    
class PresentAddressListCreateView(ListCreateAPIView):
    queryset = PresentAddressIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PresentAddressSerializer
    
class PresentAddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PresentAddressIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PresentAddressSerializer
    

class PermanentAddressListCreateView(ListCreateAPIView):
    queryset = PermanentAddressIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PermanentAddressSerializer
    
class PermanentAddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PermanentAddressIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PermanentAddressSerializer
    
    
class CompanyDetailListCreateView(ListCreateAPIView):
    queryset = CompanyDetailIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CompanyDetailSerializer
    pagination_class = CustomPagination
    
    
class CompanyDetailRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyDetailIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CompanyDetailSerializer
    
    
class Contact_infoListCreateView(ListCreateAPIView):
    queryset = Contact_infoIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = Contact_infoSerializer
    
class Contact_infoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contact_infoIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = Contact_infoSerializer
    
from Authentication.models import *

class SocialMediaLinkListCreateView(ListCreateAPIView):
    queryset = SocialMediaLinkIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SocialMediaLinkSerializer
    
class SocialMediaLinkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SocialMediaLinkIT.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SocialMediaLinkSerializer
    
class SocialMediaListCreateAPIView(ListCreateAPIView):
    queryset = SocialMediaLink.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SocialMediaSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response("Social media created")
    
    
    
# ----------------------------header views---------------------------

class siteListCreateView(ListCreateAPIView):
    queryset = siteList.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = siteListSerializer

class siteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = siteList.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = siteListSerializer
    
    
class NavbarCreateView(ListCreateAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NavbarSerializer
    
    def create(self, request, *args, **kwargs):
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(site=site_it)
            return Response({"type": "success", "msg": "Header section succesfully created"})
        return Response({"type": "error", "msg": "Header section creation failed"})
    
    def get(self,request):
        site_it = siteList.objects.get(name='IT')
        queryset = Navbar.objects.filter(site=site_it)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class NavbarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NavbarSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(site=site_it)
            return Response({"type": "success", "msg": "Header section succesfully updated"})
        return Response({"type": "error", "msg": "Header section updation failed"})
    
    
# ------------------------footer views-------------------------

class footerSectionListCreateView(ListCreateAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSectionSerializer
    
    def create(self, request, *args, **kwargs):
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(site=site_it)
            return Response({"type": "success", "msg": "Footer section succesfully created"})
        return Response({"type": "error", "msg": "Footer section creation failed"})
    def get(self, request):
        site_it = siteList.objects.get(name='IT')
        queryset = footerSection.objects.filter(site=site_it)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        
    
class footerSectionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSectionSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(site=site_it)
            return Response({"type": "success", "msg": "Footer section succesfully updated"})
        return Response({"type": "error", "msg": "Footer section updation failed"})

        
    
    
    
class footerItemListCreateView(ListCreateAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerItemSerializer
    
    def create(self, request, *args, **kwargs):
        section = request.data['footerSection']
        footer_section = footerSection.objects.filter(id=section).first()
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(footerSection=footer_section)
            return Response({"type": "success", "msg": "Footer item succesfully created"})
        return Response({"type": "error", "msg": "Footer item creation failed"})
    
    def get(self, request):
        dataArray = []
        if siteList.objects.filter(name='IT').exists():
            site_civil = siteList.objects.get(name='IT')
        if footerSection.objects.filter(site =site_civil).exists():
            allData =  footerSection.objects.filter(site =site_civil).all().order_by('-id')
        
            for section in allData:
                item = footerItem.objects.filter(footerSection=section).all()
                item_serializer = footerItemSerializer(item, many=True).data
            
                for i in item_serializer:
                    dataArray.append(i)
        return Response(dataArray)
    

class footerItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerItemSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # id = request.data['footerSection']
        # footer_section = footerSection.objects.get(id=id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Footer item successfully updated"})
        return Response({"type": "error", "msg": "Footer item updation failed"})
    
    
class footerHeadOfficeListCreateView(ListCreateAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerHeadOfficeSerializer
    
    def create(self, request, *args, **kwargs):
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(siteList=site_it)
            return Response({"type": "success", "msg": "Head office succesfully created"})
        return Response({"type": "error", "msg": "Head office  creation failed"})
    def get(self, request, *args, **kwargs):
        site_it = siteList.objects.get(name='IT')
        queryset = footerHeadOffice.objects.filter(siteList=site_it).all().order_by('-id')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class footerHeadOfficeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerHeadOfficeSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(siteList=site_it)
            return Response({"type": "success", "msg": "Head office succesfully updated"})
        return Response({"type": "error", "msg": "Head office updation failed"})

    

class footerSocialIconListCreateView(ListCreateAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSocialIconSerializer
    def create(self, request, *args, **kwargs):
        site_it = siteList.objects.get(name='IT')
        serializer = self.get_serializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(siteList = site_it)
            return Response({"type": "success", "msg": "Social icon succesfully created"})
        return Response({"type": "error", "msg": "Social icon creation failed"}) 
    def get(self,request):
        site_it = siteList.objects.get(name='IT')
        queryset = footerSocialIcon.objects.filter(siteList=site_it).order_by('-id')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
       
class footerSocialIconRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSocialIconSerializer
    lookup_field = 'pk'
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Social icon successfully updated"})
        return Response({"type": "error", "msg": "Social icon updation failed"})

    
class PaymentIconListCreateView(ListCreateAPIView):
    queryset = PaymentIcon.objects.all().order_by('-id')
    permission_classes = [IsAdminUser]
    serializer_class = PaymentIconSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Payment method succesfully created"})
        return Response({"type": "error", "msg": "Payment method creation failed"})
    
class PaymentIconRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentIcon.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PaymentIconSerializer
    lookup_field = 'pk'
    
    def partial_update(self, request,pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Footer item successfully updated"})
        return Response({"type": "error", "msg": "Footer item updation failed"})
    
    
class NewsLetterListCreateView(ListCreateAPIView):
    queryset = NewsLetter.objects.all().order_by('-id')
    permission_classes = [IsAdminUser]
    serializer_class = NewsLetterSerializer
    
class NewsLetterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = NewsLetter.objects.all().order_by('-id')
    permission_classes = [IsAdminUser]
    serializer_class = NewsLetterSerializer
    

class GlobalListCreateAPIView(ListCreateAPIView):
    queryset = GlobalLoc.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = GlobalLocSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)      
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Global location succesfully created"})
        return Response({"type": "error", "msg": "Global location creation failed"})
    
    
class GlobalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = GlobalLoc.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = GlobalLocSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Global location successfully updated"})
        return Response({"type": "error", "msg": "Global location updation failed"})
    
class PaymentMethodListCreateView(ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PaymentMethodSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)      
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Payment method succesfully created"})
        return Response({"type": "error", "msg": "Payment method creation failed"})
    
    
class PaymentMethodRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PaymentMethodSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Payment method succesfully updated"})
        return Response({"type": "error", "msg": "Payment method updation failed"})
    
class CompanyAccountListCreateView(ListCreateAPIView):
    queryset = CompanyAccount.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CompanyAccountSerializer
    
    def post(self, request, format=None):
        payment_method = request.data['payment_method']
        method_model = PaymentMethod.objects.get(method_name=payment_method)
        serializer = self.get_serializer(data=request.data or request.FILES, partial=True)
        if serializer.is_valid():
            serializer.save(payment_method=method_model)
            return Response({'type': 'success', 'msg': 'Account created successfully'})
        return Response({'type': 'error', 'msg': 'Account creation failed'})
    
    
class CompanyAccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyAccount.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CompanyAccountSerializer
    
    def partial_update(self, request, *args, **kwargs):
        payment_method = request.data['payment_method']
        method_model = PaymentMethod.objects.get(method_name=payment_method)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save(payment_method=method_model)
            return Response({"type": "success", "msg": "Company account succesfully updated"})
        return Response({"type": "error", "msg": "Company account updation failed"})
    
class CompanyAccountActive_Disable(UpdateAPIView):
    queryset = CompanyAccount.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CompanyAccountSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Company account status Changed"})
        return Response({"type": "error", "msg": "Company account updation failed"})      

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser = False, is_staff = False).order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    
class OrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.all().order_by('-id')
    
class PendingOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='pen').order_by('-id')
    
class PaymentOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='pay').order_by('-id')
    
class WorkingOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='wor').order_by('-id')
    
class CancelledOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='can').order_by('-id')
    
class CompletedOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='com').order_by('-id')
    
class DeliveryOrderListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OrderItSerializer
    queryset = OrderIt.objects.filter(status='del').order_by('-id')


class TransactionListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TransactionModel_Serializer
    queryset = TransactionModel.objects.all()

    def get(self,request):
        trans =  TransactionModel.objects.all().order_by('-id')
        return Response(self.serializer_class(trans,many=True ,context={'request':request}).data )

