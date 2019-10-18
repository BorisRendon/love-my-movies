#!/usr/bin/env python3
from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import json
import requests

#api_key = 0f90dc240d06fa41a1a68cbc6abd44af

developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")
#todas las peliculas
#peliculas = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=0f90dc240d06fa41a1a68cbc6abd44af&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1')
#peliculas_json = peliculas.json()
#print(peliculas_json)
joker_movie = requests.get("https://api.themoviedb.org/3/movie/475557?api_key=0f90dc240d06fa41a1a68cbc6abd44af")
joker_movie_json=joker_movie.json()


with open('joker_movie_details.json' , 'r') as myfile:
    data = myfile.read()

#parsear file
obj = json.loads(data)

print("Original title: " + str(obj['original_title']))
print("Overview: " + str(obj['overview']))



app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('layout.html')
if __name__ == '__main__':
    app.run(debug=True)


