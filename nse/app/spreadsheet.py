import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheets(object):

    scope = ['https://spreadsheets.google.com/feeds']

    def __init__(self):
        # Use credentials to create a client to interact with the Google
        # Drive API
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'nse/app/client_secret.json', self.scope)
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
    # spread_sheet.append_row(["Hello", "There", "You", "How", "Have", "You"])

print "Done"
