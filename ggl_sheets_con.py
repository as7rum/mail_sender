from pprint import pprint

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'credentials.json'
spreadsheet_id = '1EVNnoIIubqSfja2GJfbjyDAkmWefNoOzH-vG6Y-_-_g'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, 
    ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http = httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    range = 'A1:AF5',
    majorDimension = 'ROWS'
).execute()


# pprint(type(values['values']))
# pprint(values['values'].count())

# values = service.spreadsheets().values().get()