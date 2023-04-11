import requests
import bs4
import configparser
from detachedhouse.detached_house_rent import DetachedHouseRentApi
from standorg.stand_org import StandOrgApi

from comm.service_key import CommProperty
import xml.etree.ElementTree as et


def ops():
    properties = configparser.ConfigParser()
    properties.read('C:/workspace_python/config.ini')    
    serviceKey = properties.get('DATAGO', 'SERVICE_KEY')

    # url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade"

    # params = {
    #     'serviceKey': serviceKey,
    #     'LAWD_CD': '11110',
    #     'DEAL_YMD': '202301'
    # }

    url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade?" + "serviceKey=" + serviceKey + "&LAWD_CD=11110&DEAL_YMD=202301"

    headers = {
        'Cookie': 'ROUTEID=.HTTP1'
    }

    # response = requests.request("GET", url, headers=headers, params=params)

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def apartment():
    properties = configparser.ConfigParser()
    properties.read('C:/workspace_python/config.ini')    
    serviceKey = properties.get('DATAGO', 'SERVICE_KEY')
    serviceKey = 'L4gYnZoZLFJ1j8ndrPu178xFf68Qq1jjVvYl3WPLQe7ulWqrScchcRURtE+hC/LNCvX+9K6a2C2kU1cymBniwQ=='

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade'
    params = {
        'serviceKey': serviceKey,
        'LAWD_CD': '11110', 'DEAL_YMD': '201512'}
    response = requests.get(url, params=params)
    print(response.content)
    print(response.text)


def shortsell():
    properties = configparser.ConfigParser()
    properties.read('C:/workspace_python/config.ini')    
    serviceKey = properties.get('DATAGO', 'SERVICE_KEY')
    serviceKey = 'L4gYnZoZLFJ1j8ndrPu178xFf68Qq1jjVvYl3WPLQe7ulWqrScchcRURtE+hC/LNCvX+9K6a2C2kU1cymBniwQ=='

    url = 'http://openapi.onbid.co.kr/openapi/services/KamcoPblsalThingInquireSvc/getKamcoPbctCltrList'
    params = {
        'serviceKey': serviceKey,
        'numOfRows': '10', 'pageNo': '1',
        'DPSL_MTD_CD': '0001',
        'CTGR_HIRK_ID': '10000',
        'CTGR_HIRK_ID_MID': '10100', 'SIDO': '강원도', 'SGK': '인제군', 'EMD': '남면', 'GOODS_PRICE_FROM': '522740000',
        'GOODS_PRICE_TO': '617393000', 'OPEN_PRICE_FROM': '522740000', 'OPEN_PRICE_TO': '617393000', 'CLTR_NM': '종이팩',
        'PBCT_BEGN_DTM': '20171218', 'PBCT_CLS_DTM': '20171218', 'CLTR_MNMT_NO': '2012-1141-001291'}
    response = requests.get(url, params=params)
    print(response.content)


def auction():
    cookies = {'WMONID': 'GeKwMfYFCp6', 'daepyoSiguCd': '', 'mvmPlaceSidoCd': '', 'mvmPlaceSiguCd': '',
                             'rd1Cd': '', 'rd2Cd': '', 'realVowel': '35207_45207', 'roadPlaceSidoCd': '',
                             'roadPlaceSiguCd': '', 'vowelSel': '35207_45207', 'daepyoSidoCd': '',
                             'toMul': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8%2C20200130110695%2C1%2C20230411%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20210130001266%2C1%2C20230328%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20190130038616%2C1%2C20230328%2CB%5E',
                             'realJiwonNm': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8', 'page': 'default20',
                             'JSESSIONID': 'Fhv1Nbx6Obudfg5XLh9u9wGBZJCTcxmgzXVSTT56mTaovIKmxp5gcuxaavkRwb40.amV1c19kb21haW4vYWlzMQ==', }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded', 'Content-Type': 'application/json',
        'Cookie': 'WMONID=GeKwMfYFCp6; daepyoSiguCd=; mvmPlaceSidoCd=; mvmPlaceSiguCd=; rd1Cd=; rd2Cd=; realVowel=35207_45207; roadPlaceSidoCd=; roadPlaceSiguCd=; vowelSel=35207_45207; daepyoSidoCd=; toMul=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8%2C20200130110695%2C1%2C20230411%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20210130001266%2C1%2C20230328%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20190130038616%2C1%2C20230328%2CB%5E; realJiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8; page=default20; JSESSIONID=Fhv1Nbx6Obudfg5XLh9u9wGBZJCTcxmgzXVSTT56mTaovIKmxp5gcuxaavkRwb40.amV1c19kb21haW4vYWlzMQ==',
        'Origin': 'https://www.courtauction.go.kr', 'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
        'Sec-Fetch-Dest': 'frame', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"', 'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"', }
    data = 'bubwLocGubun=1&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&notifyLoc=on&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2023&saSer=&ipchalGbncd=000331&termStartDt=2023.03.31&termEndDt=2023.04.14&lclsUtilCd=&mclsUtilCd=&sclsUtilCd=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'
    response = requests.post('https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf', cookies=cookies,
                             headers=headers, data=data, )
    bs = bs4.BeautifulSoup(response.text)
    list = bs.find_all('tr', 'Ltbl_list_lvl0') + bs.find_all('tr', 'Ltbl_list_lvl1')
    for main in list:        bb = main.find_all('td')
    aa = 0


def auction_detail():


    cookies = {'WMONID': 'GeKwMfYFCp6', 'daepyoSiguCd': '', 'mvmPlaceSidoCd': '',
                                    'mvmPlaceSiguCd': '', 'rd1Cd': '', 'rd2Cd': '', 'realVowel': '35207_45207',
                                    'roadPlaceSidoCd': '', 'roadPlaceSiguCd': '', 'vowelSel': '35207_45207',
                                    'daepyoSidoCd': '',
                                    'toMul': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8%2C20200130110695%2C1%2C20230411%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20210130001266%2C1%2C20230328%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20190130038616%2C1%2C20230328%2CB%5E',
                                    'page': 'default20',
                                    'JSESSIONID': 'YmNuB0tMIex8ggrx1DVVuaIn6AxHGK39zKWYNe43y12Oppq1xVyWNijXhR2NT4H3.amV1c19kb21haW4vYWlzMQ==',
                                    'realJiwonNm': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8',
                                    'locIdx': '202101300025001', }

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'WMONID=GeKwMfYFCp6; daepyoSiguCd=; mvmPlaceSidoCd=; mvmPlaceSiguCd=; rd1Cd=; rd2Cd=; realVowel=35207_45207; roadPlaceSidoCd=; roadPlaceSiguCd=; vowelSel=35207_45207; daepyoSidoCd=; toMul=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8%2C20200130110695%2C1%2C20230411%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20210130001266%2C1%2C20230328%2CB%5E%BA%CE%C3%B5%C1%F6%BF%F8%2C20190130038616%2C1%2C20230328%2CB%5E; page=default20; JSESSIONID=YmNuB0tMIex8ggrx1DVVuaIn6AxHGK39zKWYNe43y12Oppq1xVyWNijXhR2NT4H3.amV1c19kb21haW4vYWlzMQ==; realJiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8; locIdx=202101300025001',
    'Origin': 'https://www.courtauction.go.kr',
    'Referer': 'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf', 'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"', 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"', }
    data = 'saNo=20210130002500&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8'
    response = requests.post('https://www.courtauction.go.kr/RetrieveRealEstCarHvyMachineMulDetailInfo.laf',
                         cookies=cookies, headers=headers, data=data, )
    print(response.text)

    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent'
    params = {
        'LAWD_CD': '11110', 'DEAL_YMD': '202301'}
    response = requests.get(url, params=params)
    print(response.content)
    print(response.content)


# auction_detail()
# shortsell()
# apartment()
# ops()

def main():
    CommProperty()

    # shortsell()
    apartment()

    # api_call = DetachedHouseRentApi()
    # # api_call = StandOrgApi()


    # st = api_call.rent_cost()
    # tree = et.fromstring(st)
    # bb = tree.find('response')

    # print('a')



if __name__ == '__main__':
    main()
