# Get-Weather
A simple cli application, written in python, to display weather info on the command line.

Usage: `get-wether [zipcode]`

Requirements to build: snapd, git, Python 3, and an API key from [openweathermap.org](https://openweathermap.org/api).

Once you have your API key, create a file named 'env.py' `touch env.py`. In it add a variable called `api_key`.
```python
api_key='hereYouPlaceYourAPIKey'
```
Or:
```bash
touch env.py && echo "api_key = 'yourApiKeyHere'" > env.py
```
The script imports the `api_key` variable and uses it in all API requests.

Using Snap, install snapcraft and multipass: 
```bash
sudo snap install snapcraft && sudo snap install multipass
```
To build the snap, simply run `snapcraft` from the project directory. Note: The build process may take a few minutes
to complete.

To install the created snap:
```bash
sudo snap install *.snap --devmode
```
For more info on Snaps, see the [Snpacraft documentation for Python apps](https://snapcraft.io/docs/python-apps).