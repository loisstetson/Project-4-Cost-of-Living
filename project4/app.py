import pandas as pd
import numpy as np
import datetime as dt

from matplotlib import style
import matplotlib.pyplot as plt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask,jsonify, render_template,json

# engine = create_engine()

# Base = automap_base()

# #Way to reference

# session = Session(engine)

# #Query

# session.close()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')
    

@app.route('/Visuals')
def Visuals ():

    return render_template('visuals.html')

@app.route('/HousingCost')
def HousingCost ():

    return render_template('housing_cost_choropleth.html')


if __name__ == '__main__':
    app.run(debug=True)

