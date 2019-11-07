#!/usr/bin/env python3
from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import json
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie


#titulo, release date, popularidad , link a mas información


app = Flask(__name__)

tmdb = TMDb()
tmdb.api_key = '0f90dc240d06fa41a1a68cbc6abd44af'

movie = Movie()
popular_pelis = movie.popular()


##prueba
recomended_pelis = movie.recommendations(movie_id=111)

lista_recomended_titulos = []
lista_recomended_release_date=[]
lista_recomended_popularity=[]
lista_recomended_imagenes=[]
for r in recomended_pelis:
    titulos = str(r.title)
    release_date = str(r.release_date)
    popularity = str(r.popularity)
    imagenes = str(r.poster_path)



    lista_recomended_titulos.append(titulos)
    lista_recomended_release_date.append(release_date)
    lista_recomended_popularity.append(popularity)
    lista_recomended_imagenes.append(imagenes)

    cantidad = (len(titulos))

##

#resultado de todas las peliculas famosas
lista_populares_titulos = []
lista_populares_release_date=[]
lista_populares_popularity=[]
lista_populares_imagenes=[]
for p in popular_pelis:
    titulos = str(p.title)
    release_date = str(p.release_date)
    popularity = str(p.popularity)
    imagenes = str(p.poster_path)



    lista_populares_titulos.append(titulos)
    lista_populares_release_date.append(release_date)
    lista_populares_popularity.append(popularity)
    lista_populares_imagenes.append(imagenes)
    
   
    w = (len(titulos))


#print(w)

#top 5 movies
#joker---------------------------
jok = movie.details(475557)
joker_title = jok.title
#joker_overview = jok.overview
joker_release_date =str(jok.release_date)
#joker_votos = str(jok.vote_count)   
joker_popularity = str(jok.popularity)
joker_image = str(jok.poster_path)
#-----------------------------------------

#avengers
avengers = movie.search('Avengers: Endgame')
lista_avengers = []
for av in avengers:
    avengers_titulo = av.title
    avengers_release_date = str(av.release_date)
    avengers_popularity = str(av.popularity)
    avengers_image = str(av.poster_path)

    lista_avengers.append(avengers_titulo)
    lista_avengers.append(avengers_release_date)
    lista_avengers.append(popularity)
    lista_avengers.append(avengers_image)

#dora
dora = movie.search('Dora and the Lost City of Gold')
lista_dora = []
for dor in dora:
    dora_title = dor.title
    dora_release_date = str(dor.release_date)
    dora_popularity = str(dor.popularity)
    dora_image = str(dor.poster_path)

    lista_dora.append(dora_title)
    lista_dora.append(dora_release_date)
    lista_dora.append(dora_popularity)
    lista_dora.append(dora_image)
    
    #dora_votos = (dor.vote_count)
    #dora_overview = dor.overview


#deadpool2
deadpool2 = movie.details(383498)
deadpool_title = deadpool2.title
deadpool_release_date =str(deadpool2.release_date)
deadpool_popularity = deadpool2.popularity
deadpool_image = str(deadpool2.poster_path)
#deadpool_votos = str(deadpool2.vote_count)
#deadpool_overview = deadpool2.overview

#pulp fiction
pulp_fiction = movie.details(680)
pulp_title = pulp_fiction.title
pulp_release_date = str(pulp_fiction.release_date)
pulp_popularity = str(pulp_fiction.popularity)
pulp_image = str(pulp_fiction.poster_path)

 

#lista del joker
lista_joker = []
lista_joker.append(joker_title)
lista_joker.append(joker_release_date)
lista_joker.append(joker_popularity)
lista_joker.append(joker_image)


#lista avengers

#lista dora

#lista deadpool
lista_deadpool=[]
lista_deadpool.append(deadpool_title)
lista_deadpool.append(deadpool_release_date)
lista_deadpool.append(deadpool_popularity)
lista_deadpool.append(deadpool_image)

#lista pulp
lista_pulp = []
lista_pulp.append(pulp_title)
lista_pulp.append(pulp_release_date)
lista_pulp.append(pulp_popularity)
lista_pulp.append(pulp_image)

lista_peliculas = [lista_joker, lista_avengers, lista_dora, lista_deadpool, lista_pulp]
lista_trending_movies = [lista_populares_titulos, lista_populares_release_date , lista_populares_popularity]
lista_recomnded_movies =[lista_recomended_titulos, lista_recomended_release_date , lista_recomended_popularity]
#print(lista_trending_movies)

@app.route('/')
def index():

    
    return render_template('layout.html'  , w=w,cantidad=cantidad,lista_peliculas=lista_peliculas,lista_populares_titulos=lista_populares_titulos,lista_populares_release_date=lista_populares_release_date,lista_populares_popularity=lista_populares_popularity,lista_populares_imagenes=lista_populares_imagenes,lista_recomended_titulos=lista_recomended_titulos,lista_recomended_release_date=lista_recomended_release_date,lista_recomended_popularity=lista_recomended_popularity,lista_recomended_imagenes=lista_recomended_imagenes)
if __name__ == '__main__':
  app.run(debug=True)

#def titulos_pelis():
   # return render_template('cards.html',lista_joker=lista_joker)

