import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Add the credentials to access the Google Sheets API
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the spreadsheet
spreadsheet = client.open_by_url('YOUR_SPREADSHEET_URL')
worksheet = spreadsheet.get_worksheet(0)  # Assuming the data is in the first sheet

# Open the database file to append the text
with open('database.md', 'a') as db_file:
    # Iterate over each row in the worksheet
    for row in worksheet.get_all_records():
        if row['Generated text'] != '':
            # Write the text to the database file
            db_file.write(f"{row['Topic']},{row['Length']},{row['Style']},{row['Generated text']}\n")
            # Erase the text in the spreadsheet
            worksheet.update_cell(row['Index'], 4, '')

