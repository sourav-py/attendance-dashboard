# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/studentmodel/"


files = {'file': open('/home/sourav/Documents/', 'rb')}

r = requests.post(url, files=files)

# data to be sent to api 
data = {'username':'student_a1', 
		'password': 'passlogin',
		'first_name':'Robot',
		'last_name' : 'A',} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
print(r)

