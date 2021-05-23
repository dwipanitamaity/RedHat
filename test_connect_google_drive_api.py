import requests

URL = "https://drive.google.com/drive"

############################################################################
# Description: Establishing a successful connection with Google Drive API for
# downloading the file/s
# Author: Dwipanita Maity
# Date : 23-05-2021
# Reference : https://developers.google.com/drive/api
#############################################################################

if __name__ == "__main__":
    print("Connect to Google Drive API to Download files")
    try:
        session = requests.session()
        response = session.get(URL, stream=True)
        status = response.status_code
        print (status)
        assert status == 200
        print("PASSED: Successfully established a connection with Google Drive API")

    except Exception:
        print("PASSED: Failed to connect withGoogle Drive API")
        assert False

    
   
   
   
   
   
   
   
   
   
   



   
   
   
   




   
   
   







