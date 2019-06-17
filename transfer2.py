# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/samplemodelfile/"


files = {'files': open('/home/sourav/Documents/SampleModel_0.csv', 'rb')}



# data to be sent to api 


# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, files  = files) 
print(r)

