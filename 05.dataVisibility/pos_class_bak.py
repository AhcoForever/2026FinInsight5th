import pandas as pd
from datetime import datetime
import os


class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} --- {self.price:,}원"


class Table:
    def __init__(self, table_no):
        self.table_no = table_no
        self.orders = []

    # 테이블 총액 구하기
    def get_total(self):
        total = 0
        for order in self.orders:
            total += order.menu.price * order.amount
        return total

    # 테이블 청소
    def clear(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        table = "=" * 20
        table += "\n"
        table += f"={self.table_no:<16} = \n"
        table += "=" * 20
        table += "\n"
        if len(self.orders) == 0:  # 주문 내역이 없다 = 빈테이블
            total += f"{"EMPTY:16"}"
        else:
            table += f"= {self.get_total():<14,}원 = \n"
        table += "=" * 20
        table += "\n"
        return table


class Order:
    def __init__(self, menu, amount):
        self.menu = menu
        self.amount = amount


class POS:
    def __init__(self):
        self.sales_file = "sales_history.csv"
        self.menu_file = "menu_list.csv"
        self.setting_file = "setting.csv"
        self.tables = []
        self.menus = []
        self.is_service = False
        self.init_system

    def init_system(self):
        if os.path.exists(self.menu_file):
            menu_df = pd.read_csv(self.menu_file, header=None, names=["name", "price"])
            for _, row in menu_df.iterrows():
                menu = Menu(row["name"], int(row["price"]))
                self.menus.append(menu)
        # 세팅 파일
        if os.path.exists(self.setting_file):
            setting_df = pd.read_csv(self.setting_file, header=None, names=["table"])
            if not setting_df.empty:
                table_cnt = int(setting_df["table"].iloc[0])
                self.create_table(table_cnt)

    # 영업 시작
    def start_service(self):
        self.is_service = True

    # 영업 종료
    def end_service(self):
        # ToDo: 남아 있는 테이블 강제 계산
        self.is_service = False

    # 테이블 생성
    def create_table(self, table_cnt):
        self.tables = [Table(i + 1) for i in range(table_cnt)]

    # 메뉴 생성
    def add_menu(self, name, price):
        m = Menu(name, price)
        self.menus.append(m)

    # 메뉴 수정
    def edit_menu(self, menu_idx, new_name, new_price):
        self.menus[menu_idx].name = new_name
        self.menus[menu_idx].price = new_price

    # 메뉴 삭제
    def remove_menu(self, menu_idx):
        del self.menus[menu_idx]

    # 메뉴 리스트 출력
    def show_menus(self):
        if self.menus:

            for i, menu in enumerate(self.menus):
                print(f"{i + 1}. {menu}")
        else:
            print("메뉴 없음")

    # 테이블 현황 출력
    def show_tables(self):
        for table in self.tables:
            print(table)

    # 주문하기
    # Todo: 메뉴, 수량, 테이블번호
    def create_order(self, menu_idx, amount, table_no):
        menu = self.menus[menu_idx]
        order = Order(menu, amount)
        self.tables[table_no - 1].add_order(order)

    # 종료 시 저장
    def shutdown(self):
        menu_data = []
        for menu in self.menus:
            menu_data.append(
                {
                    "name": menu.name,
                    "price": menu.price,
                }
            )
        df = pd.DataFrame(menu_data)
        df.to_csv(
            self.menu_file,
            mode="w",
            index=False,
            header=False,
            encoding="utf-8-sig",
        )

        setting_data = {"table": len(self.tables)}
        df = pd.DataFrame(setting_data)
        df.to_csv(
            self.setting_file,
            mode="w",
            index=False,
            header=False,
            encoding="utf-8-sig",
        )

    # 결제하기
    def checkout(self, table_no):
        table = self.tables[table_no - 1]

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sales_data = []

        for o in table.orders:
            sales_data.append(
                {
                    "datatime": now,
                    "table_no": table_no,
                    "menu_name": o.menu.name,
                    "price": o.menu.price,
                    "amount": o.amount,
                }
            )
        df = pd.DataFrame(sales_data)
        # 파일이 존재하면
        if os.path.exists(self.sales_file):
            df.to_csv(
                self.sales_file,
                mode="a",
                index=False,
                header=False,
                encoding="utf-8-sig",
            )
        else:
            df.to_csv(
                self.sales_file,
                mode="w",
                index=False,
                header=False,
                encoding="utf-8-sig",
            )
        table.clear()
