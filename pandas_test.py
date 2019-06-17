import pandas as pd
from datetime import datetime
import requests

datetime_var = datetime.now()
date = datetime_var.day
month = datetime_var.month


csvfile = "/home/sourav/Documents/attendance_1.csv"
data = pd.read_csv(csvfile)

username_list = []
attendance_list = []

for i in data['id']:
    username_list.append(str(i))
for i in data[str(date)]:
    attendance_list.append(str(i))

k = 0
for i in range(0,len(data['id'])):
    if str(attendance_list[i]) != 'nan':
        k = k+1

print(k)
for i in range(0,len(data['id'])):
    username = username_list[i]
    attendance_temp = attendance_list[i]
    if str(attendance_temp) == 'nan':
        attendance = 'Absent'
    else:
        attendance = attendance_temp
    data = {
        'username':username,
        'attendance':attendance,
        'day': 'day' + str(date),
        'month':str(month),
    }
    print(data)
    r = requests.post('http://sourav2k.pythonanywhere.com/api-view/attendance/',data = data)
    print(r)
    
       
    
    