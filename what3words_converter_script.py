#Brendan Schneider
#bschneider60

#what3words-converter

#Set up what3words connection using your own API key
import what3words
api_key = 'REPLACE_WITH_KEY'
geocoder = what3words.Geocoder(api_key)

#Prompt the user for the three words they have
word1 = input("What is your first word? ")
word2 = input("What is your second word? ")
word3 = input("What is your third word? ")
three_word_address = word1 + "." + word2 + "." + word3

#Use the words provided to get a location
results = geocoder.convert_to_coordinates(three_word_address)
nearest_place = results['nearestPlace']
country = results['country']

#Convert the coordinates to the additional formats
lat_decimal_degrees = results['coordinates']['lat']
lng_decimal_degrees = results['coordinates']['lng']

lat_degrees = int(lat_decimal_degrees)
lng_degrees = int(lng_decimal_degrees)

if lat_decimal_degrees < 0:
    lat_decimal_minutes = lat_decimal_degrees * -1 % 1 * 60
else:
    lat_decimal_minutes = lat_decimal_degrees % 1 * 60
    
if lng_decimal_degrees < 0:
    lng_decimal_minutes = lng_decimal_degrees * -1 % 1 * 60
else:
    lng_decimal_minutes = lng_decimal_degrees % 1 * 60

lat_minutes = int(lat_decimal_minutes)
lng_minutes = int(lng_decimal_minutes)

lat_decimal_seconds = lat_decimal_minutes % 1 * 60
lng_decimal_seconds = lng_decimal_minutes % 1 * 60

#Print the location information
print('The coordinates of ' + three_word_address + ' are near ' + nearest_place + ', ' + country)
print()
print('Decimal Degrees')
print('Latitude: '  + str(round(lat_decimal_degrees, 4)) + '°')
print('Longitude: ' + str(round(lng_decimal_degrees, 4)) + '°')
print()
print('Degrees Decimal Minutes')
print('Latitude: '  + str(lat_degrees) + '°' + str(round(lat_decimal_minutes, 4)) + '\'')
print('Longitude: ' + str(lng_degrees) + '°' + str(round(lng_decimal_minutes, 4)) + '\'')
print()
print('Degrees Minutes Seconds')
print('Latitude: '  + str(lat_degrees) + '°' + str(lat_minutes) + '\'' + str(round(lat_decimal_seconds, 4)) + '"')
print('Longitude: ' + str(lng_degrees) + '°' + str(lng_minutes) + '\'' + str(round(lng_decimal_seconds, 4)) + '"')
