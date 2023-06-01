from flask import Flask, render_template, request, abort, Response
import json

# Libraries to help with reading and manipulating data
import pandas as pd
import numpy as np
from windrose import WindroseAxes
# Libaries to help with data visualization
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import seaborn as sns
sns.set()
import glob
# Code to ignore warnings from function usage
import warnings;
import numpy as np
warnings.filterwarnings('ignore')

app = Flask(__name__)
@app.route("/")
#data preprocecing
def wind_plot():
    file = pd.read_csv('_wind.csv')
    columnNames=file.columns.values
    dataWeather=file.to_dict('records')
    
   



    return render_template('index.html', title='Wind App', colnames=columnNames, records=dataWeather)