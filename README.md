# ER:LC API Wrapper
The first Python API wrapper for the ER:LC API.

> [!IMPORTANT]\
> Full coverage of the ER:LC API as of July 20th 2024.

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
- [x] Dynamic Rate Limiting

## Installation
First you need to install the package.

```
pip install erlcpy
```

## Setup
Setup is easy:

```python
from erlcpy import command

# Define your API credentials
base_url = "https://api.policeroleplay.community/v1" # !! Never change this !!
server_key = "your_server_key" # API key from a ER:LC server
global_api_key = "your_global_key" # !! Remove if unnecessary !!

# Instantiate the objects

## Create an instance of the Command class to use command related functions
command_api = Command(base_url, server_key) # Add global_api_key if necessary (normally not)

## Create an instance of the Information class to use information related functions
info_api = Information(base_url, server_key) # Add global_api_key if necessary (normally not)
```

Now you can start using the API - here are some examples:

```python
# Create an instance of the Command Class with your credentials
command_api = Command(base_url, server_key)

# Use the send_command method to send a remote command
try:
    response = command_api.send_command(":kick missile") #Example

    # Handle the API's Response
    if response:
        print(f"Command sent successfully. {response}")
except Exception as e:
    # Handle any Errors
    print(f"An error occurred: {e}")
```
```python
# Create an instance of the Information class
info_api = Information(base_url, server_key) # Add global_api_key if necessary (normally not)

try:
    # Use the get_queue method to retrieve the queue information of your server
    queue_info = info_api.get_queue()

    # Handle the queue information
    if queue_info:
        print("Queue information:")
        print(queue_info)
        print(f"Queue info: {queue_info}")
    else:
        print("Failed to retrieve queue information.")
except Exception as e:
    # Print the error message
    print(f"An error occurred: {e}")
```
### Classes and their methods:

#### `Remote Commands`
##### Create an instance ( command_api = Command(base_url, server_key) )
- `command_api.send_command(command)`

#### `Logs`
- `get_join_logs()`
- `get_command_logs()`
- `get_kill_logs()`
- `get_bans()`
- `get_mod_calls()`

#### `Information`
##### Create an instance ( info_api = Information(base_url, server_key) )
- `info_api.get_server_info()`
- `info_api.get_players()`
- `info_api.get_queue()`
- `info_api.get_vehicles()`


## Links
### [erlcPY Package](https://pypi.org/project/erlcpy/)
### [PRC API Documentation](https://apidocs.policeroleplay.community/reference/api-reference)


## Credits
Head Developer - [Missile05](https://discord.com/users/591298352344334388)

Documentation Inspiration - [0xRaptor](https://twitter.com/0xRaptorRblx)

Documentation/Former Project Lead - [Arimuon](https://discord.com/users/1148923243097497600)

Former Collaborator - [Yodmin](https://discord.com/users/430480677058772992)
