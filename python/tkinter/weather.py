import json

import requests  # Non-standard library
from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`

# Create root with title and favicon
root = Tk()
root.title("Weather App Exercise")
root.iconbitmap("images/favicon.ico")

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

    # Parse API content
    city = api_content[0]["ReportingArea"]
    quality = str(api_content[0]["AQI"])
    category = api_content[0]["Category"]["Name"]

    # Background colour based on AQI
    if category == "Good":
        background_colour = "#0C0"
    elif category == "Moderate":
        background_colour = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        background_colour = "#FF9900"
    elif category == "Unhealthy":
        background_colour = "#FF0000"
    elif category == "Very Unhealthy":
        background_colour = "#990066"
    elif category == "Hazardous":
        background_colour = "#660000"

    # Update program colour
    root.configure(background=background_colour)

    # Add API content to Label
    lbl_text = city + " Air Quality: " + quality + " (" + category + ")"
    lbl = Label(
        root, 
        text=lbl_text,
        font=("Helvetica", 20),
        background=background_colour
    )
    lbl.grid(row=0, column=0, padx=10, pady=10)
except Exception as e:
    aqi_content = "Error..."



# Main loop
root.mainloop()