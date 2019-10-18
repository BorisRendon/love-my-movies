#!/usr/bin/env python3
from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import json
import requests

#api_key = 0f90dc240d06fa41a1a68cbc6abd44af

developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")
#todas las peliculas
peliculas = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=0f90dc240d06fa41a1a68cbc6abd44af&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1')
peliculas_json = peliculas.json()
#print(peliculas_json)

#muestra todos los elementos que quiero de las peliculas
for pelis in peliculas_json['results']:

    titulos_pelis = (pelis['title'])
    votos_pelis = str((pelis['vote_count']))
    release_pelis =str((pelis['release_date']))
    print(titulos_pelis+ " \ncantidad de votos: =>" + votos_pelis+ "\n fecha de lanzamiento :" +release_pelis)

    y=(len(pelis))
 

print(y)


joker_movie = requests.get("https://api.themoviedb.org/3/movie/475557?api_key=0f90dc240d06fa41a1a68cbc6abd44af")
joker_movie_json=joker_movie.json()


shawshank_movie = requests.get("https://api.themoviedb.org/3/movie/278?api_key=0f90dc240d06fa41a1a68cbc6abd44af&language=en-US")
shawshank_movie_json = shawshank_movie.json()



with open('joker_movie_details.json' , 'r') as myfile:
    data = myfile.read()

#parsear file
obj = json.loads(data)
joker_title = (str(obj['original_title']))





app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('layout.html'  , y=y)
if __name__ == '__main__':
    app.run(debug=True)


class Movies():
    def top_movies(self):
        return 'aqui van las top movies'
    def all_movies(self):
        return 'aqui van las que van abajo'



