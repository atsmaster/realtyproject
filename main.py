from detachedhouse.detached_house_rent import DetachedHouseRentApi
from apart.apart_transaction import ApartRentApi
from standorg.stand_org import LawDongApi

from comm.key_property import CommProperty
import xml.etree.ElementTree as et

from auction.auction_data import AuctionData



def main():
    import urllib.parse

    encoded_str = '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8'

    decoded_str = urllib.parse.unquote(encoded_str, encoding='euc-kr')

    print(decoded_str)

    strs = decoded_str
    stre = urllib.parse.quote(strs, encoding='euc-kr')

    print(stre)

    # CommProperty()

    # 아파트
    # api_call = ApartRentApi()
    # aa = api_call.transaction_price()

    # 다가구
    # api_call = DetachedHouseRentApi()
    # st = api_call.rent_cost()

    # 법정동코드
    # law_dong_api = LawDongApi()
    # law_dong_list = law_dong_api.req_to_list()
    # law_dong_api.list_to_csv(law_dong_list)

    auction = AuctionData()
    # ac = auction.auction_detail()
    action_list = auction.get_auction_list()




    print('a')


if __name__ == '__main__':
    main()
