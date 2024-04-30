# sqlalchemy-challenge
# Climate Analysis and Exploration

This Challenge is designed to help plan a dream vacation to Honolulu, Hawaii, by providing insights into the area's climate patterns.

## Overview

The goal of this project is to perform a detailed climate analysis and data exploration for Honolulu, Hawaii. Using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib will check the climate database to uncover weather trends that will guide the vacation planning.

## Getting Started

## Part 1: Analyze and Explore the Climate Data

 Use Python and SQLAlchemy to perform basic climate analysis and data exploration. Followed the steps outlined in the `climate_starter.ipynb` notebook, which guided me through the analysis process.

### Key Steps

1. **Precipitation Analysis:** Analyze the last 12 months of precipitation data.
2. **Station Analysis:** Explore the weather station data to find the most active stations and observe temperature trends.

## Part 2: Design Your Climate App

Used Flask to create a climate API based on the queries you developed in Part 1. The API will serve the results of your analysis as JSON endpoints.

### Key Routes

- `/`: Home page listing all available routes.
- `/api/v1.0/precipitation`: Precipitation data for the last 12 months.
- `/api/v1.0/stations`: List of weather stations.
- `/api/v1.0/tobs`: Temperature observations for the most active station over the last year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Temperature statistics for a given time period.

## Running the Flask App

To start the Flask app, navigate to the app's directory and run:
```
python app.py
```
Visit `http://127.0.0.1:5000/` in your web browser to access the API.

## Acknowledgments

- Class examples and tutorials that provided insight
- Xpert Virtual Assistant for assistance
