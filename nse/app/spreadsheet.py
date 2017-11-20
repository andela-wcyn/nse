import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import os.path


class GoogleSpreadSheets(object):

    scope = ['https://spreadsheets.google.com/feeds']
    gs_client_secret = {
        "type": os.getenv('GS_TYPE'),
        "project_id": os.getenv('GS_PROJECT_ID'),
        "private_key_id": os.getenv('GS_PRIVATE_KEY_ID'),
        "private_key": os.getenv('GS_PRIVATE_KEY'),
        "client_email": os.getenv('GS_CLIENT_EMAIL'),
        "client_id": os.getenv('GS_CLIENT_ID'),
        "auth_uri": os.getenv('GS_AUTH_URI'),
        "token_uri": os.getenv('GS_TOKEN_URI'),
        "auth_provider_x509_cert_url": os.getenv(
            'GS_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url": os.getenv('GS_CLIENT_X509_CERT_URL')
    }
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        # Use credentials to create a client to interact with the Google
        # Drive API
        # Check if client_secret.json file exists
        file_path = os.path.join(self.BASE_DIR, 'client_secret.json')
        print "File: ", file_path
        if os.path.isfile(file_path):
            print "Is File!!!"
            self.credentials = ServiceAccountCredentials\
                .from_json_keyfile_name(file_path, self.scope)
        else:
            print "Is not file!!!"
            self.credentials = ServiceAccountCredentials\
                .from_json_keyfile_dict(self.gs_client_secret, self.scope)
        self.client = gspread.authorize(self.credentials)

        # Find a workbook by name and open the first sheet
        self.sheet = self.client.open("NSE Stocks").sheet1

    def append_row(self, data):
        rows_len = self.sheet.row_count
        self.sheet.insert_row(data, rows_len+1)

    def get_all_records(self):
        # Extract and print all of the values
        return self.sheet.get_all_records()


if __name__ == "__main__":
    spread_sheet = GoogleSpreadSheets()
