
from .OrderSerializer import *
from rest_framework.views import *
from rest_framework.generics import  *
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *
from .OrderModel import *


class CreateOrderViewCivil(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOrderCivilSerializer

    def post(self, request, format=None):
        try:
            userID = request.data['user']
            productID = request.data['ProductIT']
            if User.objects.filter(id=userID).exists():
                user = User.objects.get(id=userID)
            else:
                return Response({"type":"error","msg":"User not found"})    
            
            if ProductModel.objects.filter(id=productID).exists():
                product = ProductModel.objects.get(id=productID)
            else:
                return Response({"type":"error","msg":"Product not found"})
        except:    
            return Response({"type":"error","msg":"User or Product not sent with request"})    
        
      
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=user,ProductCivil=product)
        else:
            return Response({"type":"error","msg": "order data not valid"})
        
        
        # personal_info
        perData = request.data.get('personal_info[is_same]')
        if perData == False:
            personal_info = PersonalInfoSerializer(data=request.data.get('personal_info'))
            if personal_info.is_valid():
                personal_info.save(OrderCivil = order)
        else:
            personal_info = PersonalInfoCivil()
            personal_info.OrderCivil = order
            personal_info.save()

        # present_address
        preData = request.data.get('present_address[is_same]')
        if preData == False:
            present_address = PresentAddressSerializer(data=request.data.get('present_address'))
            if present_address.is_valid():
                present_address.save(OrderCivil = order)
        else:
            present_address = PresentAddressCivil()
            present_address.OrderCivil = order
            present_address.save()
        
        
        # permanent_address
        perDataADD = request.data.get('permanent_address[is_same]')
        if perDataADD == False:
            permanent_address = PermanentAddressSerializer(data=request.data.get('permanent_address'))
            if permanent_address.is_valid():
                permanent_address.save(OrderCivil = order)
        else:
            permanent_address = PermanentAddressCivil()
            permanent_address.OrderCivil = order
            permanent_address.save()

        

        # company_details
        comDetail = request.data.get('company_details[is_same]')
        if comDetail == False:
            company_details = CompanyDetailSerializer(data=request.data.get('company_details'))
            if company_details.is_valid():
                company_details.save(OrderCivil = order)
        else:
            company_details = CompanyDetailCivil()
            company_details.OrderCivil = order
            company_details.save()

        

        # contact_info
        con_info = request.data.get('contact_info[is_same]')
        if con_info == False:
            contact_info = Contact_infoSerializer(data=request.data.get('contact_info'))
            if contact_info.is_valid():
                contact_info.save(OrderCivil = order)
        else:
            contact_info = Contact_infoCivil()
            contact_info.OrderCivil = order
            contact_info.save()
        
        
        for ds in request.data['social_media']:
            data ={
                'name': ds['name'],
                'link': ds['link']
            }
            social_media = SocialMediaLinkSerializer(data=data, many=False)
            if social_media.is_valid():
                social_media.save(OrderCivil=order)
            else:
                return Response({"type":"error","msg": "social link data not valid"})
        return Response({"type":"success","msg":"Order Created",'order': order.id})

class OrderAndOtherPDFUpload(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            orderID = request.data['order']
            
            if OrderCivil.objects.filter(id=orderID).exists():
                order = OrderCivil.objects.get(id=orderID)
                order_pdfOne = request.data['order_pdfOne']
                order_pdfTwo = request.data['order_pdfTwo']
                order_pdfThree = request.data['order_pdfThree']
                other_pdfOne = request.data['other_pdfOne']
                other_pdfTwo = request.data['other_pdfTwo']
                other_pdfThree = request.data['other_pdfThree']
                
                if order_pdfOne:
                    data = {'file': order_pdfOne}
                    orderSerializer = OrderPdfSerializer(data=data, partial=False)
                    if orderSerializer.is_valid():
                        orderSerializer.save(OrderCivil=order)
                        
                if order_pdfTwo:
                    data = {'file': order_pdfTwo}
                    orderSerializer = OrderPdfSerializer(data=data, partial=False)
                    if orderSerializer.is_valid():
                        orderSerializer.save(OrderCivil=order)
                        
                if order_pdfThree:
                    data = {'file': order_pdfThree}
                    orderSerializer = OrderPdfSerializer(data=data, partial=False)
                    if orderSerializer.is_valid():
                        orderSerializer.save(OrderCivil=order)
                        
                if other_pdfOne:
                    data={'file':other_pdfOne}
                    other_pdfSerializer = OtherPdfSerializer(data=data, partial=False)
                    if other_pdfSerializer.is_valid():
                        other_pdfSerializer.save(OrderCivil=order)
                        
                if other_pdfTwo:
                    data = {'file': other_pdfTwo}
                    other_pdfSerializer = OtherPdfSerializer(data=data, partial=False)
                    if other_pdfSerializer.is_valid():
                        other_pdfSerializer.save(OrderCivil=order)
                        
                if other_pdfThree:
                    data = {'file': other_pdfThree}
                    other_pdfSerializer = OtherPdfSerializer(data=data, partial=False)
                    if other_pdfSerializer.is_valid():
                        other_pdfSerializer.save(OrderCivil=order)
                        
                return Response({"type": "success", "msg": "Completed Order Created"})
            else:
                return Response({"type": "error", "msg": "Order not found"})
        
        except:
            return Response({"type": "error", "msg": "Order and other pdf upload failed"})

class ViewAllSelfOrder(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = OrderCivil.objects.all()
    serializer_class = OrderCivilSerializer

    def get_queryset(self):
        user = self.request.user
        return OrderCivil.objects.filter(user=user).all().order_by('-id')