#
# Date : 2018.09.29 Sat
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : BubbleSort를 구현하는 프로그램.
#

# 7개의 숫자를 가진 list생성.
arr = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):  # 7번 입력받기 위한 반복문.
    num = int(input("숫자 입력 : "))
    arr[i] = num

for i in range(0, len(arr)):    #arr의 길이만큼, 즉 7번 반복.
    print("Step", i+1, "-----------")
    swapped = False     #반복할때 값 변동이 있는지 체크.
    for j in range(0, len(arr) - i - 1):    #단계별로 최대값이 항상 맨 끝으로 가기때문에 i를 빼줘서 비교횟수를 줄임.
        if arr[j] > arr[j+1]:   # 현재 인덱스 값이 다음 인덱스값보다 크다면 스왑해야함.
            temp = arr[j]       # 스왑
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swapped = True  #값 변경이 있으면 아직 정렬이 안되어있다는 뜻.
    print(arr)
    if swapped == False:    #스왑이 한번도 없다면 정렬완료상태.
        break
print("Sort Done")
print(arr)      #출력.

