import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up our database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# define our Flask app
app = Flask(__name__)

# define the welcome route 
@app.route('/')
# add the routing information for each of the other routes
def welcome():
    return(
        # add the precipitation, stations, tobs, and temp routes
        '''
    Welcome to the Climate Analysis API! \n
    Available Routes: \n
    /api/v1.0/precipitation \n
    /api/v1.0/stations \n
    /api/v1.0/tobs \n
    /api/v1.0/temp/start/end \n
    '''
    )

# Build a route for the percipitation analysis
@app.route("/api/v1.0/precipitation")
def precipitation():
    # add the line of code that calculates the date one year ago from the most recent date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create the stations route 
@app.route("/api/v1.0/stations")
def stations():
    # create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    # convert our unraveled results into a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the temperature route 
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # calculate the date one year ago from the last date in the database.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #  unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    return jsonify (temps=temps)

# Create a route for our summary statistics report 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # create a query to select the minimum, average, and maximum temperatures
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # Determine the starting and ending date using the if-not statement
    if not end: 
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    # calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

