import time
import requests
import pandas as pd

# Kakao API Geocoding 함수
def geocode_kakao(address, api_key):
    """
    Kakao Local API를 사용해 주소를 위도, 경도로 변환하는 함수
    :param address: 도로명 주소
    :param api_key: Kakao REST API Key
    :return: (latitude, longitude) 좌표 튜플
    """
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    headers = {"Authorization": f"KakaoAK {api_key}"}
    params = {"query": address}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        result = response.json()
        if result['documents']:
            x = float(result['documents'][0]['x'])  # 경도 (longitude)
            y = float(result['documents'][0]['y'])  # 위도 (latitude)
            return y, x
        else:
            return None, None  # 결과 없음
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, None


# apt2013_df = pd.read_csv('Data_Preprocessing/add_2013.csv', encoding="utf-8")
# apt2014_df = pd.read_csv('Data_Preprocessing/add_2014.csv', encoding="utf-8")
# apt2015_df = pd.read_csv('Data_Preprocessing/add_2015.csv', encoding="utf-8")
# apt2016_df = pd.read_csv('Data_Preprocessing/add_2016.csv', encoding="utf-8")
# apt2017_df = pd.read_csv('Data_Preprocessing/add_2017.csv', encoding="utf-8")
# apt2018_df = pd.read_csv('Data_Preprocessing/add_2018.csv', encoding="utf-8")
# apt2019_df = pd.read_csv('Data_Preprocessing/add_2019.csv', encoding="utf-8")
# apt2020_df = pd.read_csv('Data_Preprocessing/add_2020.csv', encoding="utf-8")
# apt2021_df = pd.read_csv('Data_Preprocessing/add_2021.csv', encoding="utf-8")
# apt2022_df = pd.read_csv('Data_Preprocessing/add_2022.csv', encoding="utf-8")
# apt2023_df = pd.read_csv('Data_Preprocessing/add_2023.csv', encoding="utf-8")
# apt2024_df = pd.read_csv('Data_Preprocessing/add_2024.csv', encoding="utf-8")

# # 주소 리스트가 담긴 데이터프레임 예시
# # apt2013_df ~ apt2024_df를 하나로 합치거나, 필요한 데이터프레임에서 '도로명주소'를 가져옵니다.
# # 모든 데이터프레임을 합친 예시:
# all_addresses = pd.concat([apt2013_df, apt2014_df, apt2015_df, apt2016_df, apt2017_df, 
#                            apt2018_df, apt2019_df, apt2020_df, apt2021_df, apt2022_df, 
#                            apt2023_df, apt2024_df])['도로명주소'].drop_duplicates()


import sys

year = sys.argv[1]
address_df = pd.read_csv(f'data-files/add_{year}.csv', encoding="utf-8")

# 결과 저장할 리스트
coordinates = []

for row in address_df.values[21589:21591]:

    # API Key 설정
    kakao_api_key = "d521968522a7b6e1d1d38e13e83f1320"  # Kakao REST API 키를 입력하세요

    # 지오코딩 실행
    
    lat, lng = geocode_kakao(row[2], kakao_api_key)
    coordinates.append({'no': row[0] ,'address': row[2], 'latitude': lat, 'longitude': lng})
    
    # 진행 상황 출력
    if (row[0] + 1) % 10 == 0:
        print(f"{row[0] + 1}/{address_df.shape[0]} addresses processed.")

        # 결과를 데이터프레임으로 변환
        coordinates_df = pd.DataFrame(coordinates)

        # 결과 저장
        coordinates_df.to_csv(f"data-files/geocoded_addresses_{year}.csv", index=False)

    
    # API 호출 제한을 피하기 위해 딜레이 추가 (필요시)
    time.sleep(0.3)  # 0.2초 대기 (초당 5건 요청)

# 결과를 데이터프레임으로 변환
coordinates_df = pd.DataFrame(coordinates)

# 결과 저장
coordinates_df.to_csv(f"data-files/geocoded_addresses_{year}.csv", index=False)
