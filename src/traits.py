import json

# using the clarifai API
from clarifai import rest
from clarifai.rest import ClarifaiApp

# API Key
app = ClarifaiApp(api_key='b8446d22739948508ef70da2f2051061')

model = app.models.get("general-v1.3")

# getting the url of the img to be processed 
f = open("C://Users//Sailesh Nankani//Downloads//url.txt", "r+")
imgurl = f.read()
f.close()

# the url code of the picture clarifai is analyzed. Output is a JSON object
all_traits = json.dumps(model.predict_by_url(url=imgurl))

# this converts the JSON object into a python dict
main_traits = json.loads(all_traits)

individual_traits = main_traits['outputs'][0]['data']['concepts']

# erases any previous data
with open("C://Users//Sailesh Nankani//HTV//src//attribute.txt", "w") as f:
    f.write("")
f.close()





# only picking the top 3 results
for i in range(1):
    attribute = (individual_traits[i]['name'])
    # appending the attributes data
    with open("C://Users//Sailesh Nankani//HTV//src//attribute.txt", "a") as f: 
        f.write(attribute+"\n")

f.close()











