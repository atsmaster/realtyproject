from detachedhouse.detached_house_rent import DetachedHouseRentApi
from apart.apart_transaction import ApartRentApi
from standorg.stand_org import LawDongApi

from comm.key_property import CommProperty
import xml.etree.ElementTree as et



def main():
    CommProperty()

    # 아파트
    api_call = ApartRentApi()
    aa = api_call.transaction_price()

    # 다가구
    # api_call = DetachedHouseRentApi()
    # st = api_call.rent_cost()

    # 법정동코드
    # law_dong_api = LawDongApi()
    # law_dong_list = law_dong_api.req_to_list()
    # law_dong_api.list_to_csv(law_dong_list)

    print('a')


if __name__ == '__main__':
    main()
