import pandas as pd
from datetime import date
import os


class SalesAnalyzer:
    def __init__(self):
        self.sales_file = "sales_history.csv"

    # csv 읽어오기
    def load_data(self):
        if os.path.exists(self.sales_file):
            return pd.read_csv(
                self.sales_file,
                names=["datetime", "table_no", "name", "price", "amount"],
            )
        else:
            return None

    # 일자별 매출
    def get_daily_sales(self):
        df = self.load_data()
        if df is None:
            return None

        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.date
        df["total"] = df["price"] * df["amount"]

        return df.groupby("date")["total"].sum()

    # 메뉴 탑3
    def get_top3_menus(self):
        df = self.load_data()
        if df is None:
            return None

        return df.groupby("name")["amount"].sum().sort_values(ascending=False).head(3)

    # 오늘의 매출
    def get_today_sales(self):
        df = self.load_data()
        if df is None:
            return None

        df["datetime"] = pd.to_datetime(df["datetime"])
        df["date"] = df["datetime"].dt.date
        df["total"] = df["price"] * df["amount"]

        today = date.today()
        today_data = df[df["date"] == today]

        if today_data.empty:
            return 0
        return today_data["total"].sum()
