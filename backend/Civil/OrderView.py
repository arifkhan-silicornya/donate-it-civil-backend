
from .OrderSerializer import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *
from .OrderModel import *


class CreateOrderView(APIView):
    permission_classes = [AllowAny]

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
        if personal_info.is_valid():
            personal_info.save(orderCivil = order)

        present_address = PresentAddressSerializer(data=request.data.get('present_address'))
        if present_address.is_valid():
            present_address.save(orderCivil = order)
        
        permanent_address = PermanentAddressSerializer(data=request.data.get('permanent_address'))
        if permanent_address.is_valid():
            permanent_address.save(orderCivil = order)

        company_details = CompanyDetailSerializer(data=request.data.get('company_details'))
        if company_details.is_valid():
            company_details.save(orderCivil = order)

        contact_info = Contact_infoSerializer(data=request.data.get('contact_info'))
        if contact_info.is_valid():
            contact_info.save(orderCivil = order)

        
        for some in  request.data.get('social_media'):
            social_media = SocialMediaLinkSerializer(data=some)
            if social_media.is_valid():
                social_media.save(orderCivil = order)

        for OrPDF in  request.data.get('order_pdf'):
            order_pdf = OrderPdfSerializer(data=OrPDF)
            if order_pdf.is_valid():
                order_pdf.save(orderCivil = order)

        for OtPDF in  request.data.get('other_pdf'):
            other_pdf = OtherPdfSerializer(data=OtPDF)
            if other_pdf.is_valid():
                other_pdf.save(orderCivil = order)

            
        return Response({"type":"success","msg":"Order Created"})