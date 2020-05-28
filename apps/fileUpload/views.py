from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from ftplib import FTP
from rest_framework import status
from rest_framework.response import Response
from decouple import config
from apps.fileUpload.serializers import FileUploadSerializer


class FileUploadView(CreateAPIView):
  allowed_methods = ['post']

  def create(self, request, *args, **kwargs):   
    file_to_save = request.data['file']    

    ftp_host = config("FTP_SERVER_HOST")
    ftp_user = config("FTP_SERVER_USER")
    ftp_password = config("FTP_SERVER_PASSWORD")

    # now connect ftp server and send the file
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_password)
    
    # set current working directory
    ftp.cwd('files/CoronaPhotos/')

    # ftp.encoding='utf-8'
    f = ftp.storbinary("STOR "+file_to_save.name, file_to_save, 1024)
    #keep in mind that, if any file exists with the same name then file will be replaced


    return Response(
      data={
      'status': True,
      'message': "Alhamdulillah, File uploaded !"      
      },
      status=status.HTTP_201_CREATED
    )