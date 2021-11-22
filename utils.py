from math import radians,asin, cos, sin, sqrt
def haversine_distance(lat1, lon1, lat2, lon2):
    """Return the distance in km between two points around the Earth.

    Latitude and longitude for each point are given in degrees.
    """
    lon1,lat1,lon2,lat2 = map (radians,[lon1,lat1,lon2,lat2]) #transfer the angle to the curvature
    latd = lat2 - lat1
    lond = lon2 - lon1
    t= cos(lat2)*cos(lat1)* sin(lond/2)**2 + sin(latd/2)**2
    z = asin(sqrt(t))*2
    R = 6371 # Radius of earth in kilometers
   
    return z * R
