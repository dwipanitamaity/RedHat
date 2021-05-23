from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE= 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

############################################################################
# Description: For downloading any file/image using google drive api
# the app is expecting the respective file to be present in google drive storage
# This is a basic validation to check the expected file to be present in cloud
# #
# Author: Dwipanita Maity
# Date : 23-05-2021
# Reference : https://developers.google.com/drive/api/v3/reference/files/list
#############################################################################

# Create a Google Drive Service Instance
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#Need to pass a query for extracting the files from a parent folder
page_token = None
response = service.files().list(q="mimeType='image/jpeg'",  spaces='drive', fields='nextPageToken, files(id, name)', pageToken = page_token).execute()
files = response.get('files')
if files is not None:
    df = pd.DataFrame(files)
    df = df['name']

for name in df.values:
    try:
        if str(name) == 'test.jpeg':
            print ("PASSED: The file to be downloaded from Google drive exists")
            assert True
            break

    except Exception:
        print ("FAILED: The file to be downloaded from Google drive does not exist")
        assert False

    
   
   
   
   
   
   
   
   
   
   



   
   
   
   




   
   
   







