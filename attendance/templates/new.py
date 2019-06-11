import pandas as pd
import numpy as np
data = pd.read_csv('/home/sourav/Documents/SampleModel_0.csv')

print(data.head())

id_variable = data.iloc[[0],[0]]
#print(np.array(id).flatten())
movie = data.iloc[[0],[1]]
IMDB = data.iloc[[0],[2]]
print(np.array(movie['movie']))
print(np.array(IMDB['IMDB']))

print(str(np.array(movie['movie'])[0]))

print(len(data))

for i in data.values:
    id = i[0]
    movie = i[1]
    imdb = i[2]
    print(id,movie,imdb)
  