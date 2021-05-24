import json
import os
import sys

CLIENT_SECRET_FILE = 'client_secret.json'
filepath = os.path.abspath(os.path.dirname(__file__))
client_file = os.path.join(str(filepath), CLIENT_SECRET_FILE)

####################################################################
# Description: 'client_secret file' is provided by the developed app
#              from google drive which holds the necessary details of
#              client, project, token_uri, auth_uri in order to establish
#              the service with app.This is a basic test to verify the
#              details present in the downloaded json
# Author: Dwipanita Maity
# Date : 23-05-2021
####################################################################

if __name__ == "__main__":
    if client_file:
        try:
            with open(str(client_file)) as data_file:
                data = json.load(data_file)
                project_id = data['installed']['project_id']  # u'integral-glass-314505'
                # client_id = data['installed']['client_id']  #u'241533224810-leth62jvplsbjdckq28vbkqe5t9psisq.apps.googleusercontent.com'
                token_uri = data['installed']['token_uri']  # u'https://oauth2.googleapis.com/token'
                auth_uri = data['installed']['auth_uri']  # u'https://accounts.google.com/o/oauth2/auth'

                assert project_id == 'integral-glass-314505'
                assert token_uri == 'https://oauth2.googleapis.com/token'
                assert auth_uri == 'https://accounts.google.com/o/oauth2/auth'

            print ("PASSED: Verified Client_Secret file holds all necessary information to establish a service")
            assert True

        except Exception as e:
            print ("FAILED: Client_Secret file does not hold necessary information to establish a service with app")
            assert False
