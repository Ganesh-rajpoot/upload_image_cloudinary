from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UploadImage,FileUpload
from .serializers import UploadSerializer
from rest_framework  import status
from rest_framework.parsers import MultiPartParser, JSONParser
# Create your views here.
import cloudinary
class UploadView(APIView):
    parser_classes = (MultiPartParser,JSONParser,)
    
    @staticmethod
    
    def post(request):
        file = request.data.get('image')

        upload_data = cloudinary.uploader.upload(file)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)

    # def post(self,request):
    #     file = UploadImage.objects.get('image')
    #     print("imagee",file)
    #     serializer  = UploadSerializer(data= request.data)
        
    #     if serializer.is_valid():
            
    #         upload_data = cloudinary.uploader.upload(file)
    #         # serializer.save()
    #         return Response({'status': 'success','data': upload_data,}, status=201)
    #         print("file uploaded successfully")
    #         return Response({'msg':'File Uploaded Successfully'},status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_200_OK)
class FileView(APIView):
    parser_classes = (MultiPartParser,JSONParser,)
    
    @staticmethod

    def post(self,request,format=None):
        files = request.data.get('file')
        print("filess",files)
        upload_data = cloudinary.uploader.upload(files)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)