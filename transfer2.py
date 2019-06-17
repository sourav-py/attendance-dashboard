# importing the requests library 
import requests 
import pandas as pd

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/attendance/"
csvfile = "/home/sourav/Documents/SampleModel_0.csv"
#print(csvfile['movie'])
data = pd.read_csv(csvfile)
for i in data.values:
	id = i[0]
	print(id)
	movie = i[1]
	print(movie)
	imdb = i[2]
	print(imdb)
	data = {
		'movie':movie,
		'IMDB':imdb,
	}
	r = requests.post(url = API_ENDPOINT , data= data)
	print(r)

