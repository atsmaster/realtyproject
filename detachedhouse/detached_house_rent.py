import requests
from comm.key_property import CommProperty
import xml.etree.ElementTree as ET


class DetachedHouseRentApi():
    # 국토교통부_단독/다가구 전월세 자료

    def __init__(self):
        print("init")
        self.base_url = ''

    def rent_cost(self):
        url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent'
        params = {
            'serviceKey': CommProperty().service_key,
            'LAWD_CD': '11110',
            'DEAL_YMD': '202301',
            'type': 'json'
        }
        response = requests.get(url, params)
        print(response.text)


        root = ET.fromstring(response.text)
        tree = ET.ElementTree(root)
        tree.write("example.xml",encoding="UTF-8")

        return response.text

