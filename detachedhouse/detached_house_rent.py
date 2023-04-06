from comm.service_key import CommProperty
import requests
from urllib.parse import urlencode


class DetachedHouseRentApi():

    def __init__(self):
        print("init")
        self.base_url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent'

    def rent_cost(self):
        params = {
            'LAWD_CD': '11110',
            'DEAL_YMD': '202301',
            'type': 'json'
        }
        url = self.base_url + '?serviceKey=' + CommProperty().service_key + '&' + urlencode(params)
        response = requests.get(url)
        return response.text

