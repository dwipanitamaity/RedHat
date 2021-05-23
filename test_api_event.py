
from Google import Create_Service

CLIENT_SECRET_FILE= 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
API= 'https://www.googleapis.com/drive'

############################################################################
# Description: After a having a successful connection established with Google
#              drive api,verify the correct API triggers the correct event,
#              not calls unexpected API/event
# Author: Dwipanita Maity
# Date : 23-05-2021
#############################################################################

# Create a Google Drive Service Instance
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids=['11ESqS31tPRW0HUfIDbjD8aF_VfxyKjek']
file_names=['test.jpeg']

for file_id in file_ids:

    request = service.files().get_media(fileId=file_id)
    try:
        uri = str(request.uri)
        api_end_point = API+"/"+API_VERSION+"/files"
        if api_end_point in uri:
            assert True
            print("PASSED: API triggers the expected event only")

    except Exception as e:
        print("FAILED: API triggers other than the expected event")
        assert False






































