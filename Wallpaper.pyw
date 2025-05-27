import requests
import ctypes
import json
import os
import datetime

API_KEY = "DEMO_KEY"

response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")

if response.status_code == 200:
    data = json.loads(response.content)
    image_url = data["hdurl"]
    
    response = requests.get(image_url)
    
    if response.status_code == 200:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        directory = "nasa_backgrounds"
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_path = os.path.join(directory, f"nasa_background_{date}.jpg")
        
        with open("nasa_background.jpg", "wb") as f:
            f.write(response.content)
            
        with open(image_path, "wb") as f:
            f.write(response.content)
    
        
        
        
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("nasa_background.jpg"), 0x01|0x02)
        print("Hintergrundbild erfolgreich gesetzt.")
    else:
        print("Fehler beim Herunterladen des Bildes.")
else:
    print("Fehler bei der API-Anfrage.")
