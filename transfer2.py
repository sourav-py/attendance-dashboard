# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://sourav2k.pythonanywhere.com/api-view/samplemodelfile/"
csvfile = "/home/sourav/Documents/SampleModel_0.csv"
data = pd.read_csv(csvfile)
    for i in data.values:
        id = i[0]
        movie = i[1]
        imdb = i[2]
        data = {
			'movie':movie,
			'IMDB':imdb,
		}
        r = requests.post(url = API_ENDPOINT,data = data)
		print(r)


