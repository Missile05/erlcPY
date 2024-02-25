import requests

class ServerAPI:
    def __init__(self, base_url, global_api_key, server_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {global_api_key}',
            'Server-Key': server_key
        }

    def _make_get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()

    def _make_post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()

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
