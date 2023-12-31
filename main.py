import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def get_geolocation():
    try:
        # Make a request to the ipinfo.io API
        response = requests.get('https://ipinfo.io')
        # Parse the JSON response
        data = response.json()
        # Return relevant information as a dictionary
        return {
            "ip_address": data["ip"],
            "location": f"{data['city']}, {data['region']}, {data['country']}",
            "latitude": data["loc"].split(",")[0],
            "longitude": data["loc"].split(",")[1],
            "isp": data["org"]
        }
    except Exception as e:
        # Return an error message if an exception occurs
        return {"error": f"An error occurred: {e}"}

@app.get("/")
async def root():
    geolocation_data = get_geolocation()
    return geolocation_data 

@app.post("/insert")
async def post():
    return {"message": "yet another change the post route 2"}


@app.put("/update")
async def put():
    return {"message": "yet another change the put message 2"}

