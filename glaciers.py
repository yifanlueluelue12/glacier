import pandas as pd
# The Python Data Analysis Library or pandas is a tool based on NumPy 
# that was created to solve data analysis tasks. pandas incorporates a 
# large number of libraries and some standard data models to provide the 
# tools needed to efficiently manipulate large data sets. pandas provides 
# a number of functions and methods that allow us to quickly and easily 
# manipulate functions and methods that enable us to work with data quickly
#  and easily. You will soon discover that it is one of the key factors that 
# make Python a powerful and efficient environment for data analysis.

Translated with www.DeepL.com/Translator (free version)
class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        raise NotImplementedError

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
