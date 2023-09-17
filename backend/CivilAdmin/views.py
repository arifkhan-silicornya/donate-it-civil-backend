from django.shortcuts import render
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination



from Header.serializers import *
from Header.models import *

from Civil.models import *
from CivilAdmin.serializers import *

from footer.serializers import *
from footer.models import *

# Create your views here.

class SiteListView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = siteList.objects.all()
    serializer_class = SiteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'type':'success','msg': 'SiteList successfully created'}, status=status.HTTP_201_CREATED)
    
class CreateNavbarView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'type':'success','msg': 'Navbar successfully created'}, status=status.HTTP_201_CREATED)




# =======================         BannerCivil CRUD With APIView        ========================
class BannerCivilAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return BannerCivil.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = BannerCivilSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = BannerCivil.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = BannerCivilSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BannerCivilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            instance = BannerCivil.objects.get(id=pk)    
        except BannerCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BannerCivilSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated BannerCivil"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            instance = BannerCivil.objects.get(id=pk)    
        except BannerCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "BannerCivil Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "BannerCivil Successfully activated"}, status=status.HTTP_200_OK)





# =======================         FeatureWorksCategory CRUD With APIView        ========================
class FeatureWorksCategoryAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_feature_works_category(self, pk):
            return FeatureWorksCategory.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_feature_works_category(pk)
            serializer = FeatureWorksCategoryeSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = FeatureWorksCategory.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = FeatureWorksCategoryeSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FeatureWorksCategoryeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            instance = FeatureWorksCategory.objects.get(id=pk)    
        except FeatureWorksCategory.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = FeatureWorksCategoryeSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated FeatureWorksCategory"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            instance = FeatureWorksCategory.objects.get(id=pk)    
        except FeatureWorksCategory.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully activated"}, status=status.HTTP_200_OK)         
           

# =======================         FeatureWorks CRUD With APIView        ========================
class FeatureWorksAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10
    
    def get_feature_works(self, pk):
            return FeatureWorks.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_feature_works(pk)
            serializer = FeatureWorksSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = FeatureWorks.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = FeatureWorksSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        try:
            category_id = request.data['category']
        except:    
            return Response({"type":"error","msg":"Category Id not sent with request"})

        if FeatureWorksCategory.objects.filter(id=category_id).exists():
            category = FeatureWorksCategory.objects.get(id=category_id)
        else:
            return Response({"type":"error","msg":"Category not found"}) 

        serializer = FeatureWorksSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            category_id = request.data['category']
        except:    
            return Response({"type":"error","msg":"Category Id not sent with request"})

        if FeatureWorksCategory.objects.filter(id=category_id).exists():
            category = FeatureWorksCategory.objects.get(id=category_id)
        else:
            return Response({"type":"error","msg":"Category not found"}) 
        try:
            instance = FeatureWorks.objects.get(id=pk)    
        except FeatureWorks.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = FeatureWorksSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated FeatureWorks", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            instance = FeatureWorks.objects.get(id=pk)    
        except FeatureWorks.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully activated"}, status=status.HTTP_200_OK)


# =======================         Architecture CRUD With APIView        ========================
class ArchitectureAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_architecture(self, pk):
            return Architecture.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_architecture(pk)
            serializer = ArchitectureSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = Architecture.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = ArchitectureSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArchitectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            instance = Architecture.objects.get(id=pk)    
        except Architecture.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = ArchitectureSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated Architecture"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            instance = Architecture.objects.get(id=pk)    
        except Architecture.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "FeatureWorksCategory Successfully activated"}, status=status.HTTP_200_OK) 




# =======================         OurServices CRUD With APIView        ========================
class OurServicesAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return OurServices.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = OurServicesSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = OurServices.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = OurServicesSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OurServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = OurServicesSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated OurServices"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "OurServices Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "OurServices Successfully activated"}, status=status.HTTP_200_OK)


# =======================         Readmore CRUD With APIView        ========================
class ReadmoreAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return Readmore.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = ReadmoreSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = Readmore.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = ReadmoreSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ReadmoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = ReadmoreSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated Readmore"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "Readmore Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "Readmore Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         SecurityPage CRUD With APIView        ========================
class SecurityPageAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return SecurityPage.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = SecurityPageSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = SecurityPage.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = SecurityPageSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SecurityPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = SecurityPageSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated SecurityPage"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "SecurityPage Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "SecurityPage Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         Contact CRUD With APIView        ========================
class ContactPageAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return Contact.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = ContactSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = Contact.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = ContactSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = ContactSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated Contact"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "Contact Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "Contact Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         ProductCategoryModel CRUD With APIView        ========================
class ProductCategoryModelAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return ProductCategoryModel.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = ProductCategorySerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = ProductCategoryModel.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = ProductCategorySerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = ProductCategorySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated ProductCategoryModel"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "ProductCategoryModel Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "ProductCategoryModel Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         ProductModel CRUD With APIView        ========================
class ProductModelAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return ProductModel.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = ProductSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = ProductModel.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = ProductSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        try:
            category_id = request.data['category']
        except:    
            return Response({"type":"error","msg":"Product Category Id not sent with request"})

        if ProductCategoryModel.objects.filter(id=category_id).exists():
            category = ProductCategoryModel.objects.get(id=category_id)
        else:
            return Response({"type":"error","msg":"Product Category not found"}) 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        try:
            category_id = request.data['category']
        except:    
            return Response({"type":"error","msg":"Product Category Id not sent with request"})

        if ProductCategoryModel.objects.filter(id=category_id).exists():
            category = ProductCategoryModel.objects.get(id=category_id)
        else:
            return Response({"type":"error","msg":"Product Category not found"}) 
        instance = self.get_data_pk(pk)
        serializer = ProductSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated ProductModel", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "ProductModel Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "ProductModel Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         NoticeModel CRUD With APIView        ========================
class NoticeModelAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return NoticeModel.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = NoticeSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = NoticeModel.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = NoticeSerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = NoticeSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated NoticeModel"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "NoticeModel Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "NoticeModel Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         CompanyModel CRUD With APIView        ========================
class CompanyModelAPIView(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    page_size = 10

    def get_data_pk(self, pk):
            return CompanyModel.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = CompanySerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = CompanyModel.objects.all().order_by('-id')
            results = self.paginate_queryset(instance, request, view=self)
            serializer = CompanySerializer(results, many=True, context={'request':request})
        return self.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = CompanySerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated CompanyModel"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "CompanyModel Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "CompanyModel Successfully activated"}, status=status.HTTP_200_OK)   


# =======================         BottomBanner CRUD With APIView        ========================
class BottomBannerAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get_data_pk(self, pk):
            return BottomBanner.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = BottomBannerSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = BottomBanner.objects.all().order_by('-id')
            serializer = BottomBannerSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = BottomBannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = BottomBannerSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated BottomBanner"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "BottomBanner Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "BottomBanner Successfully activated"}, status=status.HTTP_200_OK)                           


# =======================         GlobalLocation CRUD With APIView        ========================
class GlobalLocationAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get_data_pk(self, pk):
            return GlobalLocation.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = GlobalLocationSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = GlobalLocation.objects.all().order_by('-id')
            serializer = GlobalLocationSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = GlobalLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = GlobalLocationSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated GlobalLocation"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "GlobalLocation Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "GlobalLocation Successfully activated"}, status=status.HTTP_200_OK)                           