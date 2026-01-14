from pos_class_bak import POS
from data_analyzer import SalesAnalyzer

if __name__ == "__main__":
    pos = POS()
    analyzer = SalesAnalyzer()

    while True:
        if pos.is_service:
            print("=" * 30)
            print("a. 가게 현황 확인")
            print("b. 금일 매출 확인")
            print("c. 주문받기")
            print("d. 계산하기")
            print("e. 영업 종료")
            choice = input("입력: ")
            if choice == "a":
                pos.show_tables()
            elif choice == "b":
                print(analyzer.get_today_sales())
            elif choice == "c":
                pos.show_tables()
                table_no = input("테이블번호 입력: ")
                pos.show_menus()
                menu_idx = input("메뉴 번호 입력: ")
                amount = input("수량 입력: ")
                pos.create_order(int(menu_idx) - 1, int(amount), int(table_no))
            elif choice == "d":
                pos.show_tables()
                table_no = input("테이블번호 입력: ")
                pos.checkout(int(table_no))
            elif choice == "e":
                pos.end_service()
        else:
            print("=" * 30)
            print("a. 테이블 수 설정")
            print("b. 메뉴 설정")
            print("c. 영업 시작")
            print("d. 통계 확인")
            print("e. 프로그램 종료")
            choice = input("입력: ")
            if choice == "a":
                table_cnt = input("테이블 수 입력: ")
                pos.create_table(int(table_cnt))
            elif choice == "b":
                print("=" * 30)
                print("a. 메뉴 추가")
                print("b. 메뉴 수정")
                print("c. 메뉴 삭제")
                sub_choice = input("입력: ")
                if sub_choice == "a":
                    menu_name = input("메뉴명 입력: ")
                    price = input("가격 입력: ")
                    pos.add_menu(menu_name, int(price))
                elif sub_choice == "b":
                    pos.show_menus()
                    if len(pos.menus) > 0:
                        menu_idx = input("메뉴 선택: ")
                        new_name = input("새메뉴명 입력: ")
                        new_price = input("새가격 입력: ")
                        pos.edit_menu(int(menu_idx) - 1, new_name, int(new_price))
                elif sub_choice == "c":
                    pos.show_menus()
                    if len(pos.menus) > 0:
                        menu_idx = input("메뉴 선택: ")
                        pos.remove_menu(int(menu_idx) - 1)
            elif choice == "c":
                pos.start_service()
            elif choice == "d":
                print(analyzer.get_daily_sales())
                print(analyzer.get_top3_menus())
            elif choice == "e":
                pos.shutdown()
                break
