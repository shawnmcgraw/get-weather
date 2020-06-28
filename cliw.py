import argparse
import requests
import json

from env import api_key


def get_weather():
    """Prints the weather. Be sure to add the zip code.

    Usage: get-weather [zip_code]"""

    parser = argparse.ArgumentParser()
    parser.add_argument("zip", help="Zip code", type=int)
    args = parser.parse_args()
    zip_code = args.zip

    url_payload = {'zip': zip_code, 'units': 'imperial', 'appid': api_key}
    req = requests.get('https://api.openweathermap.org/data/2.5/weather', params=url_payload)
    w_data = json.loads(req.text)

    if len(str(zip_code)) != 5:
        print("Invalid zip code.")
    else:
        if req.status_code == 200:
            print(f"Current Weather in {w_data['name']}")
            print(f"Condition: {w_data['weather'][0]['main']}")
            print(f"Temp: {int(w_data['main']['temp'])}F")
            print(f"Humidity: {w_data['main']['humidity']}")
        elif req.status_code == 401:
            print("Unauthorized. Please check your api key.")
        elif req.status_code == 500:
            print("Server Error!")
        else:
            print("Request error.")


if __name__ == '__main__':
    get_weather()
