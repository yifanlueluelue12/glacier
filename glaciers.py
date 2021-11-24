from utils import haversine_distance

# The Python Data Analysis Library or pandas is a tool based on NumPy 
# that was created to solve data analysis tasks. pandas incorporates a 
# large number of libraries and some standard data models to provide the 
# tools needed to efficiently manipulate large data sets. pandas provides 
# a number of functions and methods that allow us to quickly and easily 
# manipulate functions and methods that enable us to work with data quickly
#  and easily. You will soon discover that it is one of the key factors that 
# make Python a powerful and efficient environment for data analysis.
import matplotlib.pyplot as plt
from datetime import datetime
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
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        currentyear = date.strftime("%Y")
        while int(year) <= currentyear and int(year) >= 1963 and year.isdigit() == Ture:
            print('the input year is the right value')
        else:
            raise ValueError(
                "the input year in the file is a wrong number of because the detection year comes from 1963 to currentyear")

    def plot_mass_balance(self, output_path):
        plt.plot(self.year, self.mass_balance)
        plt.xlabel('year')
        plt.ylabel('mass_balance')
        plt.savefig('output_path/.png')
        plt.show()

class GlacierCollection:
    def __init__(self, file_path):
        self.file_path = file_path
        self.glacierscollection = glacierscollection
        glaciersdata = pd.read_csv(self.file_path)
        print(pd_reader)
        dataform = list(zip(glaciersdata['WGMS_ID'],glaciersdata['NAME'],glaciersdata['POLITICAL_UNIT'],
                   glaciersdata['LATITUDE'],glaciersdata['LONGITUDE'],glaciersdata['PRIM_CLASSIFIC'],
                   glaciersdata['From'],glaciersdata['FRONTAL_CHARS']))
        
    



