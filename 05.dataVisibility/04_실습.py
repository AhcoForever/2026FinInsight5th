import pandas as pd
import numpy as np
import matplotlib as plt

try:
    df = pd.read_csv(
        "/Users/kmy/StudioProjects/01_python1229/05. 데이터 시각화/avocado.csv"
    )
    print("성공")
except UnicodeDecodeError:
    print("인코딩 오류 발생")
except FileNotFoundError:
    print("파일 경로 확인 필요")
except Exception as e:
    print(f"기타 오류 발생 : {e}")

# 1. 날짜 타입 변환
df["Date"] = pd.to_datetime(df["Date"])

# 2. 월 추출
df["Month"] = df["Date"].dt.month

# 확인
print(df[["Date", "Month"]].head())

# 3. (심화) 겨울철(1,2,12월) 데이터 필터링
winter_df = df[(df["Month"] == 1) | (df["Month"] == 2) | (df["Month"] == 12)]
print(f"겨울 데이터 개수: {len(winter_df)}")

# 1. 종류 확인
print(df["type"].unique)

# 2. 그룹별 평균 가격 구하기
type_mean = df.groupby("type")["AveragePrice"].mean()

print("\n--- 아보카도 종류별 평균 가격 ---")
print(type_mean)

# 1. 종류 확인
print(df["type"].unique)

# 2. 그룹별 평균 가격 구하기
type_mean = df.groupby("type")["AveragePrice"].mean()

print("\n 아보카도 종류별 평균 가격")
print(type_mean)

# 1. 'TotalUS' 제거 (불필요한 합계 데이터 제외)
print(df["region"].unique)
df_local = df[df["region"] != "TotalUS"]

# 날짜별 전체 평균 가격 추이
daily_price = df.groupby("Date")["AveragePrice"].mean()
print(daily_price)
daily_price.plot(figsize=(12, 6), title="All Avocado Price Trend")
plt.show()

# 일반 vs 유기농 각각 그리기
pivot_df = df.pivot_table(
    index='Date',
    columns='type',
    values='AveragePrice',
    aggfunc='median'
)
print(pivot_df)

# 그래프 그리기
pivot_df.plot(figsize = (12,6), title="Conventional cs Organic Price")
plt.show()

# 연도별 평균 가격 계산
yearly_price = df.groupby('year')['AveragePRice'].mean()

# 그래프 그리기
plt.figure(figsize=(8,5))

# plt.bar(x값, y값)
plt.bar(yearly_price.index, yearly_price.values, color='forestgreen')

# 꾸미기
plt.title('Average Avocado PRice by year', fontsize=15) # 제목
plt.xlabel('Year') # x축 이름
plt.ylabel('price ($)') # y축 이름
plt.xticks(yearly_price.index) # X 축 눈금을 연도로 딱 맞춤
plt.grid(axis='y', linestyle='--',, alpha=0.7) # y축에만 점선 그리드 추가
plt.show()

# 가방 크기별 총 판매량 계산
# 각 컬럼 의 전체 합계(sum)를 구해서 리스트로 만듭니다. 
bag_sizes = ['Small Bags','Large Bags', 'XLarge Bags']
bag_sums = [df['Small Bags'].sum(),df['Large Bags'].sum(), df['XLarge Bags'].sum()]

# 그래프 그리기
plt.figure(figsize=(6,6))

# plt.pie(값, label= 이름, autopct=비율표시형식)
# autopct='%.1f%%: 소수점 첫째자리까지 %로 표시
# explode: 간격 설정
plt.pie (bag_sums, labels=bag_sizes, autopct='%.1f%%', 
         explode)
