# insertion sort
# 잡히는 대로 정렬
# 첫번째 인덱스 정렬 10
# 첫번째 인덱스와 두번째 인덱스 값 비교 후 앞에 추가할지 뒤에 추가할지 판단.

def insertion_sort(data):
    sorted = []
    while data:
        target = data[0]
        del data[0] 

        idx = 0

        for i,s in enumerate(sorted):
            inx = i
            if s > target:
                break
        sorted.insert(idx, target)
            

    return sorted

number = [10,4,2,1,5,8,6,7,3,9]
result = insertion_sort(number)
print(result)