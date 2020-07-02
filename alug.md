# Snapcraft Basics ALUG 7-2-20
### Build a snap package from a small Python module, creating a simple command line weather application

Presented by Shawn McGraw

### Meta
- What is a [snap](https://snapcraft.io/docs/getting-started)
  - Snapd  - runs in the background and manages the snap environment 
  - Snap packages - install-able package, kinda like a .deb or .rpm but with deps and assets
- Why Snaps? What problem does it solve?
  - Tries to solve the problem of developing/packaging/maintaining for different distros and environments such as apt, dnf, yum, packman... even eopkg on Solus
  - Runs on any Linus distro (MacOS too)
  - Provides app confinement and permissions control
  - Bundle assets and dependencies
  - Not getting into Snap vs Flatpak... too deep a rabbit hole
  
### The project - What we're building
- get-weather cli app, written in Python
- Objective was to improve Python coding, learn a bit about a few libraries, setuptools and snaps

### Requirements to get started
- snapd
- Python 3
- git
- [Openweathermap.org](https://openweathermap.org) api key
- text editor/IDE
- Clone Github repo: `git clone https://github.com/shawnmcgraw/get-weather`

### Building the app
- Following the [snapcraft docs](https://snapcraft.io/docs)
- Install snapcraft and multipass: `sudo snap install snapcraft --classic`
- Look at the cliw.py module
- Create env file and add api_key variable
- snapcraft.yml
  - Metadata
  - Base
  - Parts
  - Dependencies
  - Commands
- setup.py
  - py_modules
  - entry_points
- Run `snapcraft` command
- What is Multipass? - Creates a vm in which the snap is built
- Install the snap: `sudo snap install *.snap --devmode`
- Test the app: `get-weather 44221`