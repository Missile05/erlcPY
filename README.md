# ER:LC API Wrapper
An Python API wrapper for the ER:LC API.

## Capabilities:
- [x] Run ER:LC Commands Remotely
- [x] Show Server Information
- [x] Show Current Players
- [x] Show Join Logs
- [x] Show Queue Information
- [x] Show Kill logs
- [x] Show Command Logs
- [x] Show Mod Calls
- [x] Show Banned Players
- [x] Show Current Vehicles

> [!IMPORTANT]\
> Full coverage of the ERLC API as of April 8th 2024.

## Installation
First you need to install the package.

```
pip install erlcpy
```

### Setup
Setup is easy:

```python
from erlcpy import ServerAPI # Import Package

# Define your API credentials
base_url = "https://api.policeroleplay.community/v1" # Never change this
server_key = "your_server_key" # API key from a ER:LC server
global_api_key = "your_global_key" # Remove if unnecessary

# Instantiate the ServerAPI object
api = ServerAPI(base_url, server_key)
```

Now you can start using the API - here are some examples:

```python
command = "erlc_command_here" # :kill, :kick, etc
try:
    response = api.send_command(command)
    print("Command sent successfully:")
    print(response)
except Exception as e:
    print("Failed to send command:", e)
```
```python
try:
    queue = api._make_get_request('server/queue')
    print("Queue:")
    print(queue)
except Exception as e:
    print("Failed to fetch queue:", e)
```

### [erlcpy PyPi Package](https://pypi.org/project/erlcpy/)
### [PRC API Documentation](https://apidocs.policeroleplay.community/reference/api-reference)


### Credits
Project Lead - [Arimuon](https://discord.com/users/1148923243097497600)

Head Developer - [Missile05](https://discord.com/users/591298352344334388)

Collaborator - [Yodmin](https://discord.com/users/430480677058772992)

Documentation Inspiration - [0xRaptor](https://twitter.com/0xRaptorRblx)
