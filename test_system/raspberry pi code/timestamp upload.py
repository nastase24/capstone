import os
from google.auth.transport.requests import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from random import random
import time
import serial
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#AUTHOR : Alexander Nastase
# This program is intended to run as a daemon on a raspberry pi, 
# which will upload data measured from an arduino to a google sheet
# NOTE: it is not finished, and needs to be implemented functionally on a
# pi, interface correctly with the arduino, and be able to run in the background


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# add spreadsheet id here
SPREADSHEET_ID = ""

def authenticate():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("token.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    return credentials

def append_data(sheets, data):
    body = {
        "values": [[data]]
    }
    result = sheets.values().append(spreadsheetId=SPREADSHEET_ID, range="Sheet1",valueInputOption="USER_ENTERED",body=body).execute()
    print(result)    

def main():
    credentials = authenticate()
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        #ser = serial.Serial("/dev/ttyACM0", 9600)
        #define other serials in here
        #serials = [ser]
        data = []
        while True:
            data = f"{random.uniform(0,25)}, {random.uniform(0,30)}"
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_entry = f"{current_time}, {data}"
            print(data_entry)
            # append_data(sheets, data)          
    except HttpError as e:
        print(e.error_details)    

if __name__ == "__main__":
    main()        
    
    
