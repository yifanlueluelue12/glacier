from utils import haversine_distance
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path


class Glacier:
    def __init__(self, glacier_id, name, unit, lat, lon, code):
        self.year = []  # define the year as the matrix
        self.lon = lon
        self.name = name
        if float(self.lon) >= -180:  # distinguish if longitude value meets the requirement
            print(" longitude value satisfies the minimum limit")
        elif float(self.lon) <= 180:
            print("longitude value satisfies the maximum limit")
        else:
            raise ValueError
            print('the value of input longitude is an error')
        self.mass_balance = []
        self.unit = unit
        self.glacier_id = glacier_id
        if glacier_id.isdigit() == True and len(self.glacier_id) == 5:
            print('input a right glacier_id')
        else:
            print('input an error glacier_id')  # distinguish if glacier_id value meets the requirement
        self.lat = lat
        if float(self.lat) >= -90:
            print('longitude value satisfies the minimum limit')
        elif float(self.lat) <= 90:
            print('longitude value satisfies the maximum limit')
        else:
            raise ValueError
            print('the value of input longitude is an error')
        self.code = code

    def add_mass_balance_measurement(self, year, mass_balance):
        self.mass_balance =mass_balance
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        currentyear = date.strftime("%Y")
        if int(year) <= currentyear and int(year) >= 1963 and year.isdigit() == True:
            print('the input year is the right value')
        else:
            raise ValueError(
                'the input year in the file is a wrong number of because the detection year comes from 1963 to currentyear')

    def plot_mass_balance(self, output_path):
        plt.plot(self.year, self.mass_balance)
        plt.xlabel('year')
        plt.ylabel('mass_balance')
        plt.savefig('output_path/.png')
        plt.show()


class GlacierCollection:
    def __init__(self, file_path):
        self.file_path = file_path
        file_path = Path("sheet-A.csv")
        collection = GlacierCollection(file_path)
        self.collection = collection
        glacierdata_row = zip(collection['WGMS_ID'], collection['NAME'], collection['POLITICAL_UNIT']
                       , collection['LATITUDE'], collection['LONGITUDE'],collection['PRIM_CLASSIFIC'] )

        self.glacier = [Glacier(row[0], row[1], row[2], row[3], row[4], row[5]) for row in glacierdata_row]

    def read_mass_balance_data(self, file_path):
        self.file_path = file_path



    def find_nearest(self, lat, lon, n=5):
            """Get the n glaciers closest to the given coordinates."""
            distance = []
            for glacier in self.glacier:
                D = haversine_distance(lat, lon, glacier.lat, glacier.lon)
                distance.append(D)
            print(distance.index(min(distance)))

    def filter_by_code(self, code_pattern):
        """Return the names of glaciers whose codes match the given pattern."""

        raise NotImplementedError


    def sort_by_latest_mass_balance(self, n=5, reverse=True):
        """Return the N glaciers with the highest area accumulated in the last measurement."""

        raise NotImplementedError

    def summary(self):
        raise NotImplementedError

    def plot_extremes(self, output_path):
        raise NotImplementedError

