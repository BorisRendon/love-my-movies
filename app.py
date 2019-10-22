#!/usr/bin/env python3
from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import json
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie
import redis 


#titulo, release date, popularidad , link a mas información


app = Flask(__name__)




tmdb = TMDb()
tmdb.api_key = '0f90dc240d06fa41a1a68cbc6abd44af'

movie = Movie()
popular_pelis = movie.popular()


#resultado de todas las peliculas famosas, son 14
for p in popular_pelis:
    titulos = str(p.title)
    release_date = str(p.release_date)
    popularity = str(p.popularity)
   
    w = (len(titulos))
    
#top 5 movies
#joker---------------------------
jok = movie.details(475557)
joker_title = jok.title
#joker_overview = jok.overview
joker_release_date =str(jok.release_date)
#joker_votos = str(jok.vote_count)   
joker_popularity = str(jok.popularity)
#-----------------------------------------

#avengers
avengers = movie.search('Avengers: Infinity War')
for av in avengers:
    avengers_titulo = av.title
    avengers_release_date = str(av.release_date)
    avengers_popularity = str(av.popularity)
   
    
    #avengers_votos = str(av.vote_count)
    #avengers_overview = av.overview

#dora
dora = movie.search('Dora and the Lost City of Gold')
for dor in dora:
    dora_title = dor.title
    dora_release_date = str(dor.release_date)
    dora_popularity = str(dor.popularity)
    
    
    #dora_votos = (dor.vote_count)
    #dora_overview = dor.overview


#deadpool2
deadpool2 = movie.details(383498)
deadpool_title = deadpool2.title
deadpool_release_date =str(deadpool2.release_date)
deadpool_popularity = deadpool2.popularity
#deadpool_votos = str(deadpool2.vote_count)
#deadpool_overview = deadpool2.overview

#pulp fiction
pulp_fiction = movie.details(680)
pulp_title = pulp_fiction.title
pulp_release_date = str(pulp_fiction.release_date)
pulp_popularity = str(pulp_fiction.popularity)

 


lista_joker = []
lista_joker.append(joker_title)
lista_joker.append(joker_release_date)
lista_joker.append(joker_popularity)
print(lista_joker)





joker_movie = requests.get("https://api.themoviedb.org/3/movie/475557?api_key=0f90dc240d06fa41a1a68cbc6abd44af")
joker_movie_json=joker_movie.json()


shawshank_movie = requests.get("https://api.themoviedb.org/3/movie/278?api_key=0f90dc240d06fa41a1a68cbc6abd44af&language=en-US")
shawshank_movie_json = shawshank_movie.json()



@app.route('/')
def index():

    
    return render_template('layout.html'  , w=w,lista_joker=lista_joker)
if __name__ == '__main__':
  app.run(debug=True)





#class Movies():
 #   def top_movies(self):
  #      return 'aqui van las top movies'
   # def all_movies(self):
    #    return 'aqui van las que van abajo'



