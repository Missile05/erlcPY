# ER:LC API Wrapper
A Python API wrapper for the ER:LC API.

## Installation
First you need to install the package.

`pip install erlcpy`

### Setup
Setup is easy:

```python
from erlcpy import ServerAPI

# Define your API credentials
base_url = "https://api.policeroleplay.community/v1"
global_api_key = "your-global-api-key"
server_key = "your-server-key"

# Create an instance of ServerAPI with your credentials
server = ServerAPI(base_url, global_api_key, server_key)
```

Now you can start using the API - here are a example:

```python
from erlcpy import ServerAPI

# Define your API credentials
base_url = "https://api.policeroleplay.community/v1"
global_api_key = "your-global-api-key"
server_key = "your-server-key"

# Create an instance of ServerAPI with your credentials
server = ServerAPI(base_url, global_api_key, server_key)

try:
    # Get server information
    server_info = server.get_server_info()
    print("Server Information:", server_info)

except Exception as e:
    print("An error occurred:", e)
```

### [PRC API Documentation](https://apidocs.policeroleplay.community/reference/api-reference)
### [erlcpy PyPi Package](https://pypi.org/project/erlcpy/)

### Credits
Project Lead - [Arimuon](https://discord.com/users/1148923243097497600)

Head Developer - [Missile05](https://discord.com/users/591298352344334388)

Collaborator - [Yodmin](https://discord.com/users/430480677058772992)

Documentation Inspiration - [0xRaptor](https://twitter.com/0xRaptorRblx)
