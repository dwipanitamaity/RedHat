import requests
import os
import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service

CLIENT_SECRET_FILE= 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Create a Google Drive Service Instance
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ['11ESqS31tPRW0HUfIDbjD8aF_VfxyKjek']
file_names = ['test.jpeg']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    #downloader = MediaIoBaseDownload('True', request=request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        #size = 363366
    fh.seek(0)

    with open(os.path.join('./Download', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
    print("File download successful")


    
    
   
   
   
   
   
   
   
   
   
   



   
   
   
   




   
   
   







