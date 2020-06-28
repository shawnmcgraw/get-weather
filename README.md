# Get-Weather
A simple cli app written in python to display weather info from the command line.
It pulls weather info from the [Open Weather Map api](https://openweathermap.org/current).

Usage: `get-wether [zipcode]`

To use this script you'll need an [openweathermap.org](https://openweathermap.org/api) api key. It's free. 
Once you have your key, create a file named 'env.py' `touch env.py`. In it add a variable called `api_key`.
```python
api_key='hereYouPlaceYourAPIKey'
```
The script imports the `api_key` variable and uses it in all API requests.

To build the snap, simply run `snapcraft` from the directory containing the project. 
See the [Snpacraft documentation for Python apps](https://snapcraft.io/docs/python-apps).