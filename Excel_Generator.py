import xlsxwriter


data = [
        
        {
            'name': "Amy Williams",
            'phone': "892-221-4578",
            'email': "AWilliam11@gmail.com",
            'address': "24 Green St",
            'country': "Denmark"            
        },
        {
            'name': "Allen Williams",
            'phone': "312-451-4577",
            'email': "AWilliam@gmail.com",
            'address': "24 Green St",
            'country': "Denmark"            
        },
        {
            'name': "James Smith",
            'phone': "616-456-4785",
            'email': "MrSmith@gmail.com",
            'address': "122 Third St",
            'country': "England"            
        },
        {
            'name': "Tyrone Howes",
            'phone': "586-445-6541",
            'email': "Howes45@ahoo.com",
            'address': "65 Highland Rd",
            'country': "USA"            
        },
        {
            'name': "Carlos Santos",
            'phone': "313-323-0010",
            'email': "CSantos222@yahoo.com",
            'address': "123 Long St",
            'country': "USA"            
        },
        ]

workbook = xlsxwriter.Workbook("PythonExcelGenerator.xlsx")
worksheet = workbook.add_worksheet('sheet1')

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "Name")
worksheet.write(0, 2, "Phone")
worksheet.write(0, 3, "Email")
worksheet.write(0, 4, "Address")
worksheet.write(0, 5, "Country")

for index, entry in enumerate(data):
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, entry["name"])
    worksheet.write(index+1, 2, entry["phone"])
    worksheet.write(index+1, 3, entry["email"])
    worksheet.write(index+1, 4, entry["address"])
    worksheet.write(index+1, 5, entry["country"])

workbook.close()