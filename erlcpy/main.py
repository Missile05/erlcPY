import requests

class ServerAPI:
    def __init__(self, base_url, server_key, global_api_key=None):
        self.base_url = base_url
        self.server_key = server_key
        self.global_api_key = global_api_key
        self.headers = {
            'Server-Key': server_key
        }
        if global_api_key:
            self.headers['Authorization'] = f'Bearer {global_api_key}'

    def _make_get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def _make_post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

# Define the methods outside of the class
def get_server_info(self):
    return self._make_get_request('server')

def get_players(self):
    return self._make_get_request('server/players')

def get_join_logs(self):
    return self._make_get_request('server/joinlogs')

def get_queue(self):
    return self._make_get_request('server/queue')

def get_kill_logs(self):
    return self._make_get_request('server/killlogs')

def get_command_logs(self):
    return self._make_get_request('server/commandlogs')

def get_mod_calls(self):
    return self._make_get_request('server/modcalls')

def get_bans(self):
    return self._make_get_request('server/bans')

def get_vehicles(self):
    return self._make_get_request('/server/vehicles')

def send_command(self, command):
    return self._make_post_request('server/command', {'command': command})

# Bind the methods to the class
ServerAPI.get_server_info = get_server_info
ServerAPI.get_players = get_players
ServerAPI.get_join_logs = get_join_logs
ServerAPI.get_queue = get_queue
ServerAPI.get_kill_logs = get_kill_logs
ServerAPI.get_command_logs = get_command_logs
ServerAPI.get_mod_calls = get_mod_calls
ServerAPI.get_bans = get_bans
ServerAPI.send_command = send_command
ServerAPI.get_vehicles = get_vehicles