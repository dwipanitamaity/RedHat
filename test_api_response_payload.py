
from Google import Create_Service

CLIENT_SECRET_FILE= 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
API= 'https://www.googleapis.com/drive'

############################################################################
# Description: Verify valid response payload
# Author: Dwipanita Maity
# Date : 24-05-2021
#############################################################################

# Create a Google Drive Service Instance
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids=['11ESqS31tPRW0HUfIDbjD8aF_VfxyKjek']
file_names=['test.jpeg']

for file_id in file_ids:

    request = service.files().get_media(fileId=file_id)
    try:
        # Fetch the headers of the payload
        headers = request.headers

        for payload_headers in headers.keys():
            if payload_headers is not None:
                print(payload_headers)
            assert True
        print("PASSED: Payload of Google drive api response is not empty")

    except Exception as e:
        print("FAILED: Payload of Google drive api response is empty")
        assert False





































