import serial
import time
from datetime import datetime
import os
from google.auth.transport.requests import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

ser1 = serial.Serial(port='COM3', baudrate=9600,timeout=.1)

def read_from_arduinos(ports):
    #ser1.write(b"1")
    if ser1.in_waiting > 0:
        data = ser1.readline().decode('utf-8').strip()
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return (f"{now},{data}")
    else: 
        time.sleep(0.1)    
        
if __name__ == '__main__':
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # put ID here
    SPREADSHEET_ID = ""
    
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        while True:
            data = read_from_arduinos(ser1)
            if data != "":
                result = sheets.values().append(spreadsheetId=SPREADSHEET_ID, range="Sheet1",valueInputOption="USER_ENTERED").execute()
            
    except HttpError as e:
        print(e.error_details)     