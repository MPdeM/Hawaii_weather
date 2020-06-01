# HAWAII WEATHER

This project is focused on data storage and retrieval. Takes advantage of SQL, [Structured Query Languaje](https://en.wikipedia.org/wiki/SQL), to deal with relational databases. [SQLAlquemy's ORM, object-relational mapper](https://www.sqlalchemy.org/), is used to facilitate the communication between Python and databases.

![](Images/Sunset_Beach_Surfer.png)
## PROBLEM:

### Requirements 
The main requirements are: 
- Python
- Numpy
- Matplotlib
- Pandas
- SQLAlchemy and Object Relational Mapper
- datetime 

## Data
## Part 1- Data Engineering
The database [hawaii.sqlite](Resources/hawaii.sqlite) consist in two tables measurements and stations. To inspect the database use for example SQLite

![measurement](Images/measurement.png)


![stations](Images/stations.png)


The two tables are also as a csv files [hawaii_measurements.csv](Resources/hawaii_measurements.csv) and [hawaii_stations.csv](Resources/hawaii_stations.csv)

## Part 4- Results App
The data and queries can be easily presented in a FLASK API on a localy by executing the app.py from the VS terminal "> python app.py" and opening the local server http://127.0.0.1:5000/
![](Images/appexecution.png)
Routes created are:
- /api/v1.0/precipitation
  Json representation (list of dictionaries) of precipitation measurements for the last year of data in the dataset, from August 2016 to August 2017. The api data is converted into a valid json object using "jsonify".
- /api/v1.0/stations
  Json representation (list of dictionaries) of weather stations in Hawaii.
- /api/v1.0/tobs
  Json representation of the observed temperature from August 2016 to August 2017
- /api/v1.0/v1.0/temp/<start>
  Type a single date ( for example 2016-08-23) to know min, max and avg temp
- /api/v1.0/v1.0/temp/<start>/<end>
   Type a range (for example 2016-08-23/2016-08-28) to know min, max and avg temp
![api/v1.0/stations](Images/appstations.png)

