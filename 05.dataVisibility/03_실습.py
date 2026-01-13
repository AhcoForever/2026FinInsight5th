import pandas as pd
import numpy as np
import random


# 랜덤 시드 고정 (모두 같은 데이터를 갖기 위함)
np.random.seed(42)
random.seed(42)

# 1. 데이터 생성 설정 (10,000건)
num_rows = 10000

# 2. 가짜 데이터 재료
products = ["노트북", "무선마우스", "기계식키보드", "스마트폰", "모니터", "헤드셋"]
prices = [1200000, 35000, 150000, 900000, 300000, 85000]
dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="h")  # 시간 단위

# 3. 데이터 조합
data = {
    "주문번호": range(1, num_rows + 1),
    "주문일시": np.random.choice(dates, num_rows),
    "상품명": np.random.choice(products, num_rows),
    "구매자성별": np.random.choice(["남", "여"], num_rows),
    "구매자나이": np.random.randint(20, 60, num_rows),
    # 가격에 '$' 기호를 붙이고 콤마를 넣어서 '문자'로 만듦 (전처리 연습용)
    "주문금액": [f"{p:,}원" for p in np.random.choice(prices, num_rows)],
}

df = pd.DataFrame(data)

# 4. 데이터 더럽히기 (Pre-processing 연습용)
# (1) 평점 데이터 추가 (중간중간 NaN 넣기)
df["평점"] = np.random.choice(
    [1, 2, 3, 4, 5, np.nan], num_rows, p=[0.05, 0.05, 0.1, 0.3, 0.4, 0.1]
)

# (2) 주소 데이터 추가 (시/도만 랜덤 배정)
locations = ["서울", "경기", "부산", "대구", "인천", "광주", "대전"]
df["배송지"] = np.random.choice(locations, num_rows)

# 5. CSV 파일로 저장
df.to_csv("shopping_mall.csv", index=False, encoding="utf-8-sig")

print(
    f"데이터 생성 완료! 총 {num_rows}개의 주문 데이터가 'shopping_mall.csv'로 저장되었습니다."
)
# 파일 불러오기
df = pd.read_csv("shopping_mall.csv")

# 규모 확인
print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())


# 1. 주문금액 정제 (문자 -> 숫자)
df["주문금액"] = df["주문금액"].str.replace("원", "").str.replace(",", "").astype(int)

# 2. 평점 결측치 채우기
df["평점"] = df["평점"].fillna(0)

# 3. 날짜 변환
df["주문일시"] = pd.to_datetime(df["주문일시"])

# 확인
print(df.info())  # 이제 주문 금액이 int로 잡히고, 평점에 null이 없어야함

print("=" * 100)

# 1. 월별 매출 구하기

df["월"] = df["주문일시"].dt.month
monthly_sales = df.groupby("월")["주문금액"].sum()
print("월별 매출 현황")

print(monthly_sales)

# 가장 매출이 높은 월은?
max_month = monthly_sales.idxmax()
print(f"\n가장 장사가 잘 된 달은 {max_month}월 입니다.")

# 2. 지역별 구매력 확인
location_sales = df.groupby("배송지")["주문금액"].mean().sort_values(ascending=False)
print("\n---지역별 평균 주문 금액---")
print(location_sales)

item_sales = df.groupby("상품명")["주문금액"].sum().sort_values(ascending=False)
print("\n----상품별 판매 금액---")
print(item_sales)

f_df = df[(df["구매자성별"] == "여")]
print(f"여성 구매 건 수: {len(f_df)}")

m_df = df[(df["구매자성별"] == "남")]
print(f"남성 구매 건 수 : {len(m_df)}")

mf_df = pd.pivot_table(df, index="구매자성별", values="주문번호", aggfunc="count")
mf_df.dolumnw = ["주문건수"]
print(mf_df)
