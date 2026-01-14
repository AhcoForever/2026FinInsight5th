import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 1. 데이터 불러오기
# 2. csv 파일이 '|'로 구분되어 있으므로 sep='|' 옵션이 필요

df = pd.read_csv("starbucks.csv", sep="|")

# 2. 기본 지도 생성
# 데이터의 위도(Y) , 경도 (X)평균값으로 지도의 중심을 잡습니다.

map_center = [df["Ycoordinate"].mean(), df["Xcoordinate"].mean()]

m = folium.Map(location=map_center, zoom_start=7)
cluster = MarkerCluster().add_to(m)
# 3. 각 매장 위치에 마커 추가하기
for idx, row in df.iterrows():
    # 팝업에 띄울 내용 (매장명 + 주소)
    popup_content = f"""
    <div style="width:200px">
        <b>{row['Sotre_nm']}</b><br>
        <small>{row['Address']}</small>
    </div>
    """

    # 마커 생성 및 클러스터에 추가
    folium.Marker(
        location=[row["Ycoordinate"], row["Xcoordinate"]],  # [위도, 경도]
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=row["Sotre_nm"],  # 마우스 올렸을 때 나오는 이름
        icon=folium.Icon(color="green", icon="star"),  # 초록색 별 아이콘
    ).add_to(cluster)

# 4. 지도를 HTML 파일로 저장
m.save("starbucks_map.html")
print("지도가 'starbucks_map.html' 파일로 저장되었습니다.")
