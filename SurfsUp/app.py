# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.org import Session
from sqlalchemy import create_engine, func, and_
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:\\\C:\Users\Nicolette\Documents\Class_Materials\Mod_10_Challenge\sqlalchemy-challenge\SurfsUp\Resources\hawaii.sqlite")
                       
# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`

measurement = Base.classes.measurement
station = Base.classes.station

# Create a session


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
