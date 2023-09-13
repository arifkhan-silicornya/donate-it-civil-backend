
from .OrderSerializer import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *
from .OrderModel import *


class CreateOrderView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):

        try:
            userID = request.data['user']
            productID = request.data['ProductIT']
        except:    
            return Response({"type":"error","msg":"User or Product not sent with request"})    
        
        if User.objects.filter(id=userID).exists():
            user = User.objects.get(id=userID)
        else:
            return Response({"type":"error","msg":"User not found"})    
        
        if ProductModel.objects.filter(id=productID).exists():
            product = ProductModel.objects.get(id=productID)
        else:
            return Response({"type":"error","msg":"Product not found"})
      
      
        serializer = OrderItSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.save(user=user,ProductIT=product)
        else:
            return Response({"type":"error","msg": serializer.error_messages})
        
        

        personal_info = PersonalInfoSerializer(data=request.data.get('personal_info'))
        personal_info.save(orderit = order)

        present_address = PresentAddressSerializer(data=request.data.get('present_address'))
        present_address.save(orderit = order)
        
        permanent_address = PermanentAddressSerializer(data=request.data.get('permanent_address'))
        permanent_address.save(orderit = order)

        company_details = CompanyDetailSerializer(data=request.data.get('company_details'))
        company_details.save(orderit = order)

        contact_info = Contact_infoSerializer(data=request.data.get('contact_info'))
        contact_info.save(orderit = order)

        
        for some in  request.data.get('social_media'):
            social_media = SocialMediaLinkSerializer(data=some)
            social_media.save(orderit = order)

        for OrPDF in  request.data.get('order_pdf'):
            order_pdf = OrderPdfSerializer(data=OrPDF)
            order_pdf.save(orderit = order)

        for OtPDF in  request.data.get('other_pdf'):
            other_pdf = OtherPdfSerializer(data=OtPDF)
            other_pdf.save(orderit = order)

            
        return Response({"type":"success","msg":"Order Created"})