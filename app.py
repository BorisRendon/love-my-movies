#!/usr/bin/env python3
from flask import Flask, jsonify , render_template, request
import os, optparse,sys
import yaml
import requests


developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")


app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('layout.html')
if __name__ == '__main__':
    app.run(debug=True)