import requests
import json

class SwitchInfoFetcher:
    def __init__(self, ip, password):
        self.base_url = f"http://{ip}"
        self.password = password
        self.session = requests.Session()  # Create a session to persist cookies

    def login(self):
        """Send login request to the switch."""
        payload = {
            "data": {
                "callcmd": 123,  
                "calldata": {
                    "password": self.password
                }
            }
        }
        
        headers = {
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": self.base_url,
            "Referer": self.base_url,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        }

        try:
            response = self.session.post(f"{self.base_url}/123", json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            login_response = response.json()
            print("Login Response:")
            print(json.dumps(login_response, indent=4))  # Display the login response

            if login_response.get("data", {}).get("calldata", {}).get("login") == "success":
                print("Login successful.")
                return True
            else:
                print("Login failed.")
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during login: {e}")
            return False

    def fetch_switch_data(self, command):
        """Fetch data for a specific command from the switch."""
        payload = {"data": {"callcmd": command, "calldata": {}}}
        response = self.session.post(f"{self.base_url}/{command}", json=payload)

        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch switch data for command {command}: {e}")
            return None

    def fetch_all_information(self):
        """Fetch all information from the switch after logging in."""
        if not self.login():
            return  # If login failed, stop here.

        # Command fetches for port and status info
        commands = {
			'all (code 200)': 200,
			'state (code 100)': 100,
			'detail (code 101)': 101,
			'limit (code 106)': 106,
			'storm (code 107)': 107,
			'netcfg (code 108)': 108,
			'vlan (code 109)': 109,
			'mac_table (code 114)': 114,
			'LoopDetect (code 115)': 115,
			'LinkAgg (code 116)': 116,
			'SpanTree (code 117)': 117,
			'PortMirror (code 118)': 118,
			'dhcp_snoop (code 124)': 124,
        }

        all_data = {}
        for cmd_name, cmd_code in commands.items():
            print(f"Fetching {cmd_name} data...")
            data = self.fetch_switch_data(cmd_code)
            if data:
                all_data[cmd_name] = data
                print(json.dumps(data, indent=4))  

    def logout(self):
        """Logout from the switch."""
        logout_payload = {
            "data": {
                "callcmd": 126  
            }
        }
