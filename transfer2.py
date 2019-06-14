# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/post/samplemodel/"




# data to be sent to api 
data = {'movie':'John wick', 
		'IMDB': 9,} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

