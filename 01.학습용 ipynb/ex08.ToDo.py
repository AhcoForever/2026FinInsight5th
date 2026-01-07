# ToDo app
# ToDo class 의 객체 : 제목, 할일 완료 여부


class ToDo:
    def __init__(self, title):
        self.title = title
        self.is_complete = False

    def edit(self, new_title):
        self.title = new_title

    def toggle_complete(self):
        self.is_complete = not self.is_complete

    def __str__(self):
        status = "V" if self.is_complete else " "
        return f"[{status}] {self.title}"


class ToDoManager:
    def __init__(self):
        self.todos = []

    # 생성
    def create_todo(self, title):
        todo = ToDo(title)
        self.todos.append(todo)

    # 삭제
    # idx : 1 ~len(todos)
    def remove_todo(self, idx):
        del self.todos[idx - 1]

    # 수정
    # idx
    def edit_todo(self, idx, title):
        self.todos[idx - 1].edit[title]

    def check_todo(self, idx):
        self.todos[idx - 1].toggle_complete()

    # 조회
    def search_todo(self):
        for i, t in enumerate(self.todos):
            print(f"{i+1}, {t}")

    def save_to_file(self):
        with open("todo_list.txt", "w", encoding="utf-8") as f:
            for t in self.todos:
                f.write(f"{t.title}/{"T" if t.is_complete else "F"}")

    def load_by_file(self):
        try:
            with open("todo_list.txt", "w", encoding="utf-8") as f:
                for line in f:
                    data = line.split("/")
                    todo = ToDo(data[0])
                    todo.is_complete = data[1] == "T"
                    self.todos.append(todo)
        except:
            pass


def menu():
    manager = ToDoManager()
    manager.load_by_file()
    while True:
        prompt = """
            0. 종료 및 저장
            1. 조회
            2. 생성
            3. 삭제
            4. 수정
            5. 할일 체크
            """
        print(prompt)
        print("=" * 20)
        user = input("입력: ")
        if user == "1":
            manager.search_todo()
        elif user == "2":
            title = input("할일 제목 입력: ")
            manager.create_todo(title)
        elif user == "3":
            manager.search_todo()
            idx = input("지울 번호 선택: ")
            manager.remove_todo(int(idx))
        elif user == "4":
            manager.search_todo()
            idx = input("수정할 번호 선택: ")
            new_title = input("새로운 제목 입력:")
            manager.edit_todo(int(idx), new_title)
        elif user == "5":
            manager.search_todo()
            idx = input("체크할 번호 선택 :")
            manager.check_todo(int(idx))
        elif user == "0":
            manager.save_to_file()
            break


if __name__ == "__main__":
    menu()
