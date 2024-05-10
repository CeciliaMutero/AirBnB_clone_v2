#!/usr/bin/python3
places = hbnb.all("Place")
for place in places:
    hbnb.destroy(place)
