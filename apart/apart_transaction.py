import requests
from comm.key_property import CommProperty
import xml.etree.ElementTree as ET
from standorg.stand_org import LawDongApi


class ApartRentApi():
    # 국토교통부_아파트 실거래가

    def __init__(self):
        print("init")
        self.base_url = ''

    def transaction_price(self):
  
        law_dong_api = LawDongApi()
        law_dong_pd = law_dong_api.csv_to_pd()

        law_dong_cd_list = law_dong_pd['law_dong_cd'].str.slice(start=0, stop=5).unique()        

        for law_dong_cd in law_dong_cd_list:
            url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent'
            params = {
                'serviceKey': CommProperty().service_key,
                # 'LAWD_CD': law_dong_cd,
                'LAWD_CD': '41830',
                'DEAL_YMD': '202202',
                'type': 'json'
            }
            response = requests.get(url, params)
            root = ET.fromstring(response.content)
            items = root.iter('item')  # 모든 item 요소를 가져옵니다.

            vo_list = []
            for item in items:
                vo = {}
                for elem in item.iter():
                    vo[elem.tag] = elem.text
                vo_list.append(vo)


            for vo in vo_list:
                print(vo)
                if vo['월세금액'] == '0':
                    print('-----------------------')
                    print(vo)



        # root = ET.fromstring(response.text)
        # tree = ET.ElementTree(root)
        # tree.write("example.xml",encoding="UTF-8")

        return response.text
