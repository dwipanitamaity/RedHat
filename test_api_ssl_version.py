
from Google import Create_Service

CLIENT_SECRET_FILE= 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
API= 'https://www.googleapis.com/drive'

############################################################################
# Description:
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
        ssl = str(request.http.http.ssl_version)

        if ssl == 'None':
            assert True
            print("PASSED: API end point does not require any SSL certification details")

    except Exception as e:
        print("FAILED: SSL-certification has to ve taken care of by the developer")
        assert False





































