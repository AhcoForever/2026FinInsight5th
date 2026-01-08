import pandas as pd

# 행렬, Table 모양으로 데이터 처리
# 엑셀과 비슷
data = {
    "name": ["A", "B", "C", "D"],
    "age": [20, 21, 22, 23],
    "blood": ["B", "B", "A", "O"],
}
df = pd.DataFrame(data)
print(df)

print(df.index)
print(df.columns)
print(df.values)
print(type(df.values))
