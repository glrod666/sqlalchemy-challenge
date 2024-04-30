# Import necessary libraries
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Homepage Route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)  # Adjust date as per your data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    session.close()
    
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    
    stations = [station[0] for station in results]
    return jsonify(stations)

# TOBS Route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    most_active_station = 'USC00519281'  # Use your result of the most active station
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)  # Adjust date as per your data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station, Measurement.date >= one_year_ago).all()
    session.close()
    
    tobs_data = [{date: tobs} for date, tobs in results]
    return jsonify(tobs_data)

# Start Route
@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
    
    temp_list = list(results[0])
    return jsonify(temp_list)

# Start-End Route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()
    
    temp_list = list(results[0])
    return jsonify(temp_list)

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)