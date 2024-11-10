import requests


class Pushbullet:
    def __init__(self, api_key, use_device=0):
        self.api_key = api_key
        self.headers = {
            'Access-Token': self.api_key,
            'Content-Type': 'application/json'
        }
        self.device = self.get_devices()[use_device]


    def get_devices(self):
        response = requests.get('https://api.pushbullet.com/v2/devices', headers=self.headers)
        return response.json()['devices']


    def send_sms(self, addresses, message, guid=None, status=None, file_type=None, file_url=None, skip_delete_file=None):
        data = {
            "data": {
                "target_device_iden": self.device['iden'],
                "addresses": addresses,
                "message": message,
            }
        }

        if guid is not None:  data['data']['guid'] = guid
        if status is not None:  data['data']['status'] = status
        if file_type is not None:  data['data']['file_type'] = file_type
        if file_url is not None:  data['file_url'] = file_url
        if skip_delete_file is not None:  data['skip_delete_file'] = skip_delete_file

        response = requests.post('https://api.pushbullet.com/v2/texts', headers=self.headers, json=data)
        return response.json()


    def list_threads(self):
        response = requests.get(f"https://api.pushbullet.com/v2/permanents/{self.device['iden']}_threads", headers=self.headers)
        return response.json()['threads']
    

    def get_thread(self, thread_id):
        response = requests.get(f"https://api.pushbullet.com/v2/permanents/{self.device['iden']}_thread_{thread_id}", headers=self.headers)
        return response.json()


        