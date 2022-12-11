#8-6. City names: Write the city_country() function, which gets the name of the city and country.
#The function should return a string in the format “Santiago, Chile”
#Call your function for at least three city—country pairs and output the returned value.

def city_country(city,country):
    full=city+", "+country
    return full.title()
cities=city_country('london','UK')
print(cities)