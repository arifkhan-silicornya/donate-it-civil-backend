
from .OrderSerializer import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from Civil.models import *
from Civil.OrderModel import *


class CreateOrderView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):

        try:
            userID = request.data['user']
            productID = request.data['ProductCivil']
        except:    
            return Response({"type":"error","msg":"User or Product not found"})    
        
        if User.objects.filter(id=userID).exists():
            user = User.objects.get(id=userID)
        else:
            return Response({"type":"error","msg":"User not found"})    
        
        if ProductModel.objects.filter(id=productID).exists():
            product = ProductModel.objects.get(id=productID)
        else:
            return Response({"type":"error","msg":"User not found"})
      
      
        serializer = OrderCivilSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save(user=user,ProductCivil=product)
        else:
            return Response({"type":"error","msg": serializer.error_messages})
        
        

        personal_info = PersonalInfoSerializer(data=request.data.get('personal_info'))
        personal_info.save(orderCivil = order)

        present_address = PresentAddressSerializer(data=request.data.get('present_address'))
        present_address.save(orderCivil = order)
        
        permanent_address = PermanentAddressSerializer(data=request.data.get('permanent_address'))
        permanent_address.save(orderCivil = order)

        company_details = CompanyDetailSerializer(data=request.data.get('company_details'))
        company_details.save(orderCivil = order)

        contact_info = Contact_infoSerializer(data=request.data.get('contact_info'))
        contact_info.save(orderCivil = order)

        
        for some in  request.data.get('social_media'):
            social_media = SocialMediaLinkSerializer(data=some)
            social_media.save(orderCivil = order)

        for OrPDF in  request.data.get('order_pdf'):
            order_pdf = OrderPdfSerializer(data=OrPDF)
            order_pdf.save(orderCivil = order)

        for OtPDF in  request.data.get('other_pdf'):
            other_pdf = OtherPdfSerializer(data=OtPDF)
            other_pdf.save(orderCivil = order)

            
        return Response({"type":"success","msg":"Order Created"})
    

class Order_ViewSet(generics.ListAPIView):
    permission_classes = (IsAdminUser,)

    serializer_class = OrderCivilSerializer
    # serializer_class1 = FeatureWorksCategoryerializer
    # serializer_class2 = OurServicesSerializer
    # serializer_class3 = ArchitectureSerializer
    # serializer_class4 = ReadmoreSerializer
    # serializer_class5 = SecurityPageSerializer

    # serializer_class6 = ProductCategoryModelSerializer
    # serializer_class7 = NoticeSerializer
    # serializer_class8 = CompanySerializer

    def get(self, request):
        queryset = OrderCivil.objects.all()
        # queryset1 = FeatureWorksCategory.objects.filter(active=True).all()
        # queryset2 = OurServices.objects.filter(active=True).all()
        # queryset3 = Architecture.objects.filter(active=True).all()
        # queryset4 = Readmore.objects.filter(active=True).all()
        # queryset5 = SecurityPage.objects.filter(active=True).all()

        # queryset6 = ProductCategoryModel.objects.filter(active=True).all()
        # queryset7 = NoticeModel.objects.filter(active=True).all()
        # queryset8 = CompanyModel.objects.filter(active=True).all()

        return Response({
                'OrderCivil' :  self.serializer_class(queryset,many=True).data,
                # 'TechnologiesCategory' :  self.serializer_class1(queryset1,many=True).data,
                # 'OurServices' :  self.serializer_class2(queryset2,many=True).data,
                # 'atchitecture_OR_featureDesign' :  self.serializer_class3(queryset3,many=True).data,
                # 'Readmore' :  self.serializer_class4(queryset4,many=True).data,
                # 'SecurityPage' :  self.serializer_class5(queryset5,many=True).data,
                
                # 'Product' :  self.serializer_class6(queryset6,many=True).data,
                # 'Notice' :  self.serializer_class7(queryset7,many=True).data,
                # 'Company' :  self.serializer_class8(queryset8,many=True).data,
        })

    

    