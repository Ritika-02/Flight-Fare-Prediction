import sys
sys.path.append('D:\\FLIGHT_FARE_PREDICTION')


import os
import sys
from src.FlightFarePrediction.logger import logging
from src.FlightFarePrediction.exception import customexception
import pandas as pd


from src.FlightFarePrediction.components.data_ingestion import DataIngestion

obj = DataIngestion()
obj.initiate_data_ingestion()