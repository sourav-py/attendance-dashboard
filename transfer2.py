# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/studentmodel/"


files = {'file': open('/home/sourav/Documents/SampleModel_0.csv', 'r')}



# data to be sent to api 


# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, files  = files) 
print(r)

