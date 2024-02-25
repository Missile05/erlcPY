import requests

class ServerAPI:
    def __init__(self, base_url, global_api_key, server_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {global_api_key}',
            'Server-Key': server_key
        }

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = None
        if method == 'GET':
            response = requests.get(url, headers=self.headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def get_server_info(self):
        return self._make_request('GET', 'server')

    def get_players(self):
        return self._make_request('GET', 'server/players')

    def get_join_logs(self):
        return self._make_request('GET', 'server/joinlogs')

    def get_queue(self):
        return self._make_request('GET', 'server/queue')

    def get_kill_logs(self):
        return self._make_request('GET', 'server/killlogs')

    def get_command_logs(self):
        return self._make_request('GET', 'server/commandlogs')

    def get_mod_calls(self):
        return self._make_request('GET', 'server/modcalls')

    def get_bans(self):
        return self._make_request('GET', 'server/bans')

    def send_command(self, command):
        data = {'command': command}
        return self._make_request('POST', 'server/command', data)