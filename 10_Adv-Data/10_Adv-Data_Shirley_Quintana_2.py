
# import dependencies
import numpy as np
import pandas as pd
import sqlalchemy
import datetime as dt
from dateutil.relativedelta import relativedelta
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import desc

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///C:\\Users\\quint\\Desktop\\class_activities\\10_Adv-Data\\Homework_Instructions\\Resources//hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# set start date to 8/1/2017
start_date_str = '2017-08-01'
start_date = dt.datetime.strptime(
    start_date_str,'%Y-%m-%d'
)

# create variable to store previous year data
date_prior_yr = start_date - relativedelta(years=1)
print('Date from 1 year - pre year date', date_prior_yr)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd"
    )



session = Session(engine)
@app.route('/api/v1.0/precipitation')

def precipitation():
    session = Session(engine)
    precip_data = (session
                    .query(Measurement.date, Measurement.prcp)
                    .order_by(Measurement.date)
                    .all()
                    )
    precip = []
 

    for i, value in enumerate(precip_data):

        precip.append({'Date': precip_data[i][0],
        'Prcp': precip_data[i][0]
        })

    return jsonify(precip)
    

session = Session(engine)
@app.route('/api/v1.0/stations')

def stations():
    session = Session(engine)
    station_list = session.query(Measurement.station).distinct().all()
    return jsonify(station_list)


session = Session(engine)
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    station_temps = (session
                    .query(Measurement.date, Measurement.tobs)
                    .filter(Measurement.date > date_prior_yr )
                     .all()
                    )
    return jsonify(station_temps)


session = Session(engine)
@app.route('/api/v1.0/<start>/<end>')
def tempst(start,end):
    session = Session(engine)
    start_date_input = start
    end_date_input = end

    try:
        st_date_conv = dt.datetime.strptime(start_date_input, '%Y-%m-%d')
    
    except:
        print(' Invalid start date or date format. Please input valid date in yyyy-mm-dd format. ')
        print( ' Using default date.  start = 2016-08-01')
        print( 'start date input: ' + start_date_input)
        print( ' ' )
        start_date_input = '2016-08-01'
        st_date_conv = dt.datetime.strptime(start_date_input, '%Y-%m-%d')
    
    try:
        end_date_conv = dt.datetime.strptime(end_date_input, '%Y-%m-%d')

    except:
        print(' Invalid start date or date format. Please input valid date in yyyy-mm-dd format. ')
        print(' Using default end date = current date')
        print(' end date input: ' + end_date_input)
        print( ' ' )

    print(st_date_conv, end_date_conv)

    measure_temps = (session
                        .query(Measurement.date, 
                        func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                 func.max(Measurement.tobs)
                                 )
                        .filter(Measurement.date >= st_date_conv)
                        .filter(Measurement.date <= end_date_conv)
                        .group_by(Measurement.date)
                        .all()
                        )
    return jsonify(measure_temps)
    
session = Session(engine)
@app.route('/api/v1.0/<start>')
def tempStartOnly(start):
    start_date_input = start

    try:
        st_date_conv = dt.datetime.strptime(start_date_input, '%Y-%m-%d')    
     
    except:
        print(' Invalid start date or date format. Please input valid date in yyyy-mm-dd format. ')
        print(' Using default date. start = 2016-08-01')
        print(' start date input: ' + start_date_input)
        start_date_input = '2016-08-01'
        st_date_conv = dt.datetime.strptime(start_date_input, '%Y-%m-%d') 
    
    measure_start_temps = (session
                            .query(Measurement.date,
                            func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                 func.max(Measurement.tobs)
                                 )
                            .filter(Measurement.date >= st_date_conv)
                            .group_by(Measurement.date)
                            .all()
                             )
    return jsonify(measure_start_temps)     



if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
   


       







