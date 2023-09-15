import gspread

sa = gspread.service_account(filename="service_account.json") #The bot (google-sheets-service-account@vihaan-sheets.iam.gserviceaccount.com)

sheet = sa.open("Sheets API Test") #Opens sheet based on name

worksheet = sheet.worksheet("Sheet1") #Opens the worksheet tab

# Get cell's value
print(worksheet.acell("A2").value)

worksheet.update("B2", '44')