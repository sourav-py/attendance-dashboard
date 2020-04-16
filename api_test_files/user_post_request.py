# importing the requests library 
import requests 
import pandas as pd

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/studentmodel/"
csvfile = "/home/sourav/Documents/Student_0.csv"

data = pd.read_csv(csvfile)

for i in data.values:
    username = i[0]
    password = i[1]
    first_name = i[2]
    last_name = ''
    data  = {
		'username':username,
		'password':password,
		'first_name': first_name,
		'last_name':last_name,
	 }
    print(data)
    r = requests.post(url = API_ENDPOINT,data=data)
    print(r)
        