from django.shortcuts import render
from .models import Measurement
from .forms import MeasurementForm 
from geopy.geocoders import Photon
from geopy.distance import geodesic 
import geocoder
from .utils import get_center_coordinates, get_zoom
import folium 

# Calculate Distance View 
def calcDistanceView(request):
    distance = None
    destination = None 
    form = MeasurementForm(request.POST or None)
    geolocator = Photon(user_agent="measurements")

    # Location Coordinates
    g = geocoder.ip('me')
    lat = g.latlng[0]
    lon = g.latlng[1]
    location = geolocator.reverse(f"{lat}, {lon}")
    pointA = [lat, lon]
    
    # Initial Folium Map 
    m = folium.Map(width='100%', height='100%', location=get_center_coordinates(lat, lon))
    # Location Marker 
    folium.Marker([lat, lon], tooltip='Click here for more', popup=location,
                   icon = folium.Icon(color='blue', icon='home')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)

        # destination coordinates 
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)

        # calc distance 
        distance = round(geodesic(pointA, pointB).km, 2) # calc the distance

        # Destination Marker 
        m = folium.Map(width='100%', height='100%', location=get_center_coordinates(lat, lon, d_lat, d_lon), zoom_start=get_zoom(distance))
        # Location Marker 
        folium.Marker([lat, lon], tooltip='Click here for more', popup=get_center_coordinates(lat, lon),
                   icon = folium.Icon(color='blue', icon='home')).add_to(m)
        folium.Marker([d_lat, d_lon], tooltip='Click here for more', popup=destination,
                   icon = folium.Icon(color='red', icon='cloud')).add_to(m)
        
        # Draw a line between location and destination 
        line = folium.PolyLine(locations=[pointA, pointB], weight=3, color='blue')
        m.add_child(line)   # Append the Line to the Map 

        # Location 
        instance.location = location
        # Distance
        instance.distance = distance
        instance.save()
    # Map Representation
    m = m._repr_html_()
    context = {
        'distance' : distance,
        'destination' : destination,
        'form' : form,
        'map' : m,
    } 
    return render(request, 'measurements/main.html', context)

