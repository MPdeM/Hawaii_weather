#import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()


#################################################
# Flask Routes
#################################################
# define the home page and list all routes available
@app.route("/")
def main():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitaion data for the last year as json"""

    print("precipitation api")

    #Query precipitation data for the last year.First we find the last date in the database
    last_date =  session.query(Measurement.date).order_by(Measurement.id.desc()).first()
    last_datestr = last_date[0]
    last_year= int(last_datestr.split("-")[0])
    last_month= int(last_datestr.split("-")[1])
    last_day= int(last_datestr.split("-")[2])
    last_date= dt.date(last_year, last_month, last_day)
    #set beginning of search query
    date_oneyear = dt.date(last_year, last_month, last_day) - dt.timedelta(days=365)
    
    #retrieve last 12 months of data
    precp_results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date.between(date_oneyear, last_date)).all()


    #create a dictionary with the date as the key
    precip_results_dict = {}
    for x in precp_results:
        precip_results_dict[x[0]] = x[1]

    return jsonify(precip_results_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations as json."""

    print("station api")

    #query stations list
    stations_list = session.query(Station).all()

    #create a list of dictionaries
    stations_list_dict = []
    for station in stations_list:
        station_list = {}
        station_list["id"] = station.id
        station_list["station"] = station.station
        station_list["name"] = station.name
        station_list["latitude"] = station.latitude
        station_list["longitude"] = station.longitude
        station_list["elevation"] = station.elevation
        stations_list_dict.append(station_list)

    return jsonify(stations_list_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations as json"""

    print("tobs api ")

    #Query temp data for the last year.First we find the last date in the database
    last_date =  session.query(Measurement.date).order_by(Measurement.id.desc()).first()
    last_datestr = last_date[0]
    last_year= int(last_datestr.split("-")[0])
    last_month= int(last_datestr.split("-")[1])
    last_day= int(last_datestr.split("-")[2])
    last_date= dt.date(last_year, last_month, last_day)
    #set beginning of search query
    date_oneyear = dt.date(last_year, last_month, last_day) - dt.timedelta(days=365)
    
    #retrieve last 12 months of data
    temp_data = session.query(Measurement).\
        filter(Measurement.date.between(date_oneyear, last_date)).\
        all()

    #create list of dictionaries 
    temp_dict = []
    for x in temp_data:
        temp_dict[x[0]]= x[1]

    return jsonify(temp_dict)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return a JSON list of the minimum, average, and maximum temperatures from the start date until
    the end of the database."""

    print("start date api: UNDER CONSTRUCTION")

   

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a JSON list of the minimum, average, and maximum temperatures between the start date and
    the end date."""

    print("between start and end api request: UNDER CONSTRUCTION")



if __name__ == '__main__':
    app.run(debug=True)
