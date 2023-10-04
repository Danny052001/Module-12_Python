import gspread # pip install gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('18z6TprWdzEmTn2gVXZJtA1LC7HE7pAvRP1NGaTVI_s8')
worksheet = sh.sheet1

res = worksheet.get_all_records(1)
res = worksheet.get_all_values()
res = worksheet.col_values(1)
res = worksheet.get('A2:C2')
user = ["Susan", 25, "Sydney"]

worksheet.append_row(user)

worksheet.update_cell(5,2, 78)          

worksheet.delete_rows(1)               