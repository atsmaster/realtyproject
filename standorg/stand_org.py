from comm.key_property import CommProperty
from standorg.dto import LawDongDto
import requests
from fastapi.encoders import jsonable_encoder
import pandas as pd

class LawDongApi():
    # 국토교통부_전국 법정동
    def __init__(self):
        print("init")

    def req_to_list(self):
        law_dong_list = []

        requests_page=0
        while True:
            requests_page=requests_page+1
            url = 'https://api.odcloud.kr/api/15063424/v1/uddi:6d7fd177-cc7d-426d-ba80-9b137edf6066'
            params = {
                'serviceKey': CommProperty().service_key,
                'page':+ requests_page,
                'perPage':'10000'
            }
            response = requests.get(url, params)    
            response_json = response.json()

            for bjd_cd in response_json["data"]:      
                if bjd_cd['삭제일자'] is None:                
                    law_dong = LawDongDto(
                        law_dong_cd=str(bjd_cd["법정동코드"]),
                        si_do_nm=str(bjd_cd["시도명"]), 
                        si_gun_gu_nm=str(bjd_cd["시군구명"]), 
                        eup_myeon_dong_nm=str(bjd_cd["읍면동명"]), 
                        ri_nm=str(bjd_cd["리명"]), 
                        law_dong_rank=str(bjd_cd["순위"]))                
                    law_dong_list.append(law_dong)      

            if len(response_json["data"]) < 10000:
                break      

        return law_dong_list
    
    def list_to_csv(self, law_dong_list):
        law_dong_pd = pd.DataFrame(jsonable_encoder(law_dong_list))
        law_dong_pd.to_csv(CommProperty().law_dong_csv_path, encoding="utf-8-sig")


    def csv_to_pd(self):
        return pd.read_csv(CommProperty().law_dong_csv_path, dtype=object)




