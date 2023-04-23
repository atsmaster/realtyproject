from auction.dto import AuctionMaster
from dateutil.relativedelta import relativedelta
import datetime
import requests
import bs4
import urllib.parse


class AuctionData:
    def get_auction_list(self):

        auctionList = []

        jiwonNm = '서울중앙지방법원'
        jiwonNmEnc = urllib.parse.quote(jiwonNm, encoding='euc-kr')
        saYear = '2023'
        termStartDt = '2023.04.01'
        termEndDt = '2023.06.25'
        targetRowSize = 40

        targetRow = 1 - targetRowSize
        while True:
            targetRow = targetRow + targetRowSize

            response = requests.post(
                'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf',
                headers=self.get_list_url_header(),
                data=self.get_list_url_data(jiwonNmEnc, saYear, termStartDt, termEndDt, str(targetRow))
            )

            print(targetRow)

            bs = bs4.BeautifulSoup(response.text, features="html.parser")
            list = bs.find_all('tr', 'Ltbl_list_lvl0') + bs.find_all('tr', 'Ltbl_list_lvl1')
            if len(list) == 0:
                break

            for main in list:
                input_tag = main.find('input', {'name': 'chk'})
                value = input_tag['value']
                v = value.split(',')
                auctionList.append(
                    AuctionMaster(
                        jiwonNm=v[0],
                        jiwonNmEnc=jiwonNmEnc,
                        saNo=v[1]
                ))

        auctionSet = set(auctionList)

    def auction_detail(self):
        # jiwonNm = '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8'  # 서울중앙지방법원
        # saNo = '20200130003469'

        jiwonNm = '%BC%AD%BF%EF%B5%BF%BA%CE%C1%F6%B9%E6%B9%FD%BF%F8'  # 서울중앙지방법원
        saNo = '20210130001593'
        asdf = '202101301039911'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.courtauction.go.kr',
            'Referer': 'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf',
            'Sec-Fetch-Dest': 'frame',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = 'jiwonNm=' + jiwonNm + '&saNo=' + saNo + '&maemulSer=1&mokmulSer=&_NAVI_CMD=RetrieveMainInfo.laf%5EInitMulSrch.laf&_NAVI_SRNID=PNO102000%5EPNO102001&_SRCH_SRNID=PNO102001&_CUR_CMD=RetrieveRealEstMulDetailList.laf&_CUR_SRNID=PNO102002&_NEXT_CMD=RetrieveRealEstCarHvyMachineMulDetailInfo.laf&_NEXT_SRNID=PNO102015&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y&_C_srnID=PNO102000&_C_jiwonNm=' + jiwonNm + '&_C_bubwLocGubun=1&_C_jibhgwanOffMgakPlcGubun=&_C_mvmPlaceSidoCd=&_C_mvmPlaceSiguCd=&_C_roadPlaceSidoCd=&_C_roadPlaceSiguCd=&_C_daepyoSidoCd=&_C_daepyoSiguCd=&_C_daepyoDongCd=&_C_rd1Cd=&_C_rd2Cd=&_C_rd3Rd4Cd=&_C_roadCode=&_C_notifyLoc=1&_C_notifyRealRoad=1&_C_notifyNewLoc=1&_C_mvRealGbncd=1&_C_jiwonNm1=' + jiwonNm + '&_C_jiwonNm2=' + jiwonNm + '&_C_mDaepyoSidoCd=&_C_mvDaepyoSidoCd=&_C_mDaepyoSiguCd=&_C_mvDaepyoSiguCd=&_C_realVowel=00000_55203&_C_vowelSel=00000_55203&_C_mDaepyoDongCd=&_C_mvmPlaceDongCd='

        response = requests.post(
            'https://www.courtauction.go.kr/RetrieveRealEstCarHvyMachineMulDetailInfo.laf',
            headers=headers,
            data=data,
        )

        print(response.text)

    def get_list_url_data(self, jiwonNmEnc, saYear, termStartDt, termEndDt, targetRow):
        data = 'page=default40&' \
               'srnID=PNO102000&' \
               'jiwonNm=' + jiwonNmEnc + '&' \
               'jiwonNm1=' + jiwonNmEnc + '&' \
               'jiwonNm2=' + jiwonNmEnc + '&' \
               'realVowel=35207_45207&' \
               'saYear=' + saYear + '&' \
               'ipchalGbncd=000331&' \
               'termStartDt=' + termStartDt + '&' \
               'termEndDt=' + termEndDt + '&' \
               'mvRealGbncd=00031R&' \
               'srnID=PNO102001&' \
               'targetRow=' + targetRow
        return data

    def get_list_url_header(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.courtauction.go.kr',
            'Referer': 'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf',
            'Sec-Fetch-Dest': 'frame',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        return headers
