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
lista_populares_titulos = []
lista_populares_release_date=[]
lista_populares_popularity=[]
for p in popular_pelis:
    titulos = str(p.title)
    release_date = str(p.release_date)
    popularity = str(p.popularity)
    lista_populares_titulos.append(titulos)
    lista_populares_release_date.append(release_date)
    lista_populares_popularity.append(popularity)
    
   
    w = (len(titulos))


print(w)

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
avengers = movie.search('Avengers: Endgame')
lista_avengers = []
for av in avengers:
    avengers_titulo = av.title
    avengers_release_date = str(av.release_date)
    avengers_popularity = str(av.popularity)

    lista_avengers.append(avengers_titulo)
    lista_avengers.append(avengers_release_date)
    lista_avengers.append(popularity)

#dora
dora = movie.search('Dora and the Lost City of Gold')
lista_dora = []
for dor in dora:
    dora_title = dor.title
    dora_release_date = str(dor.release_date)
    dora_popularity = str(dor.popularity)

    lista_dora.append(dora_title)
    lista_dora.append(dora_release_date)
    lista_dora.append(dora_popularity)
    
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

 

#lista del joker
lista_joker = []
lista_joker.append(joker_title)
lista_joker.append(joker_release_date)
lista_joker.append(joker_popularity)


#lista avengers

#lista dora

#lista deadpool
lista_deadpool=[]
lista_deadpool.append(deadpool_title)
lista_deadpool.append(deadpool_release_date)
lista_deadpool.append(deadpool_popularity)

#lista pulp
lista_pulp = []
lista_pulp.append(pulp_title)
lista_pulp.append(pulp_release_date)
lista_pulp.append(pulp_popularity)


lista_peliculas = [lista_joker, lista_avengers, lista_dora, lista_deadpool, lista_pulp]
lista_trending_movies = [lista_populares_titulos, lista_populares_release_date , lista_populares_popularity]
print(lista_trending_movies)

@app.route('/')
def index():

    
    return render_template('layout.html'  , w=w,lista_peliculas=lista_peliculas,lista_trending_movies = lista_trending_movies,lista_populares_titulos=lista_populares_titulos)
if __name__ == '__main__':
  app.run(debug=True)

#def titulos_pelis():
   # return render_template('cards.html',lista_joker=lista_joker)

