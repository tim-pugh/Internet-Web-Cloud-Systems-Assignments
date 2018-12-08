"""
A simple guestbook flask app.
"""
import flask
from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
from index import Index
from recipe import Recipe
import google.cloud.datastore
import gbmodel
from gbmodel import model_datastore
db = model_datastore.model
import requests
from datetime import datetime
import logging



app = flask.Flask(__name__)       # our Flask app


app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/recipe/',
                 view_func=Recipe.as_view('recipes'),
                 methods=['GET', 'POST'])

app.add_url_rule('/submit/',
                 view_func=Recipe.as_view('submit'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
