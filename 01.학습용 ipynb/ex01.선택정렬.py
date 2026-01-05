# Selection Sort
# 제일 작은 수를 뽑아 뒤에 추가.
def selection_sort(data):
    sorted = []
    while data: # data가 비게되면 while문을 빠져나온다
        min_idx = 0
        for i, d in enumerate(data):
            if d < data[min_idx]:
                min_idx = i
        sorted.append(data(min_idx))
        del data[min_idx]


    return sorted

number = [10,4,2,1,5,8,6,7,3,9]
r1 = selection_sort(number)
print(f"selection sort:{r1}")