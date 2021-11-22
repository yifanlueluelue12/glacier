from utils import haversine_distance
import pandas as pd
# The Python Data Analysis Library or pandas is a tool based on NumPy 
# that was created to solve data analysis tasks. pandas incorporates a 
# large number of libraries and some standard data models to provide the 
# tools needed to efficiently manipulate large data sets. pandas provides 
# a number of functions and methods that allow us to quickly and easily 
# manipulate functions and methods that enable us to work with data quickly
#  and easily. You will soon discover that it is one of the key factors that 
# make Python a powerful and efficient environment for data analysis.
import matplotlib.pyplot as plt
import re
import datetime
class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.year=[] # define the year as the matrix
        self.lon=lon
        if float(self.lon)>=-180: # distinguish if longitude value meets the requirement
             print (' longitude value satisfies the minimum limit')
        elif float(self.lon)<=180:
             print ('longitude value satisfies the maximum limit')
        else:
             print ('the value of input longitude is an error')
        self.mass_balance=[]
        self.glacier_id = glacier_id
        if glacier_id.isdigit()== True and len(self.glacier_id)==5:
          print ('input a right glacier_id')
        else :
          print ('input an error glacier_id') # distinguish if glacier_id value meets the requirement
        self.lat=lat
        if float(self.lat)>=-90:
             print ('longitude value satisfies the minimum limit')
        elif float(self.lat)<=90:
             print ('longitude value satisfies the maximum limit')
        else:
             print ('the value of input longitude is an error')
        self.code =code

     
    def add_mass_balance_measurement(self, year, mass_balance):
        raise NotImplementedError

    def plot_mass_balance(self, output_path):
        raise NotImplementedError

        
class GlacierCollection:

    def __init__(self, file_path):
        raise NotImplementedError

    def read_mass_balance_data(self, file_path):
        raise NotImplementedError

    def find_nearest(self, lat, lon, n):
        """Get the n glaciers closest to the given coordinates."""
        raise NotImplementedError
    
    def filter_by_code(self, code_pattern):
        """Return the names of glaciers whose codes match the given pattern."""
        raise NotImplementedError

    def sort_by_latest_mass_balance(self, n, reverse):
        """Return the N glaciers with the highest area accumulated in the last measurement."""
        raise NotImplementedError

    def summary(self):
        raise NotImplementedError

    def plot_extremes(self, output_path):
        raise NotImplementedError
