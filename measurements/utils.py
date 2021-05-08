

# Helper functions 

# get center coordinates 
def get_center_coordinates(latA, longA, latB=None, longB=None):
    if latB:
        cord = [(latA + latB)/ 2, (longA+ longB)/2]
        return cord 
    

# Get Zoom 
def get_zoom(distance):
    if distance <=100:
        return 8 
    elif distance > 100 and distance <= 500:
        return 4 
    else:
        return 2  
