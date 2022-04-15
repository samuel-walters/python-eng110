import requests
# (. -- > directory)
from postcode_service.models.postcode import Postcode
from postcode_service.config_manager import base_url

class PostcodeManager:
    def __init__(self, single_postcode):
        self.url = base_url() + single_postcode
        self.request = requests.get(self.url)
        self.headers = self.request.headers
        self.response_json = self.request.json()

    def get_postcode(self):
        return Postcode(self.response_json["result"])

if __name__ == "__main__":
    pcm = PostcodeManager("B7 4BB")
    print(pcm.response_json)
    pc = pcm.get_postcode()
    print(pc)
    print(pc.parish)