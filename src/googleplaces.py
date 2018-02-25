from googleplaces import GooglePlaces, types, lang
YOUR_API_KEY = 'AIzaSyCk7Lxsu3sn8ZdbtKLe5qomTUASzRy2Dns'
google_places = GooglePlaces(YOUR_API_KEY)

# reading attributes from attributes.txt
f = open("C://Users//Sailesh Nankani//HTV//src//attribute.txt", "r+")
attribute = f.read()
f.close()

# erases any previous data
with open("C://Users//Sailesh Nankani//HTV//src//result.txt", "w") as f:
    f.write("")
f.close()

query_result = google_places.nearby_search(location='Toronto, Canada', keyword=attribute,
        radius=20000) 
if query_result.has_attributions:
    print (query_result.html_attributions)

    
for place in query_result.places:
    # Returned places from a query are place summaries.
    # place_name = place.name
    with open("C://Users//Sailesh Nankani//HTV//src//result.txt", "a") as f: 
        f.write(place.name+"\n")
    #print (place.geo_location)
    #print (place.place_id)

    # The following method has to make a further API call.
    #place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    #print (place.details) # A dict matching the JSON response from Google.
    #print (place.local_phone_number)
# for place in query_result.places:
#     website = place.website
#     with open("C://Users//Sailesh Nankani//HTV//src//result.txt", "a") as f: 
#         f.write(website+"\n")

f.close()