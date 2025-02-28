import pandas as pd
import json

#Leer el archivo JSON
df = pd.read_csv('movies_initial.csv')

#Guardar el DataFrame como JSON
df.to_json('movies.json' , orient='records')

with open('movies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break