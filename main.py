import requests
import os
import gdown
from pydrive.drive import GoogleDrive
from google_drive_downloader import GoogleDriveDownloader as gdd
from pydrive.auth import GoogleAuth
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service

def download_file_from_google_drive(id, destination):
    URL = "https://drive.google.com/drive/folders"

    session = requests.session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('__Host-GAPS'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    print("Download files from google drive")
    
    
   
                    
   
   
   
   
   
   
   
   



   
   
   
   




   
   
   







