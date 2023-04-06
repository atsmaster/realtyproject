from comm.service_key import CommProperty
import requests
from urllib.parse import urlencode


class StandOrgApi():

    def __init__(self):
        print("init")
        self.base_url = 'https://infuser.odcloud.kr/oas/docs?namespace=15063424/v1'

    def stand_org(self):
        url = self.base_url
        response = requests.get(url)
        return response.text

