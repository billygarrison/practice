import json

import requests  # Non-standard library
from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`

# Create root with title and favicon
root = Tk()
root.title("Weather App Exercise")
root.iconbitmap("images/favicon.ico")
root.configure(background="green")

# API URL
api_url = (
    "http://www.airnowapi.org/aq/observation/zipCode/current/"
    + "?format=application/json"
    + "&zipCode=02222"
    + "&distance=25"
    + "&API_KEY=0D103EE9-A34C-4291-B1A6-6D553F31BD8D"
)

# Get content from API call
try:
    api_request = requests.get(api_url)
    api_content = json.loads(api_request.content)
except Exception as e:
    aqi_content = "Error..."

# Parse API content
city = api_content[0]["ReportingArea"]
quality = str(api_content[0]["AQI"])
category = api_content[0]["Category"]["Name"]

# Add API content to Label
lbl = Label(root, text=city + " Air Quality: " + quality + " (" + category + ")", font=("Helvetica", 20), background="green")
lbl.grid(row=0, column=0, padx=10, pady=10)

# Main loop
root.mainloop()