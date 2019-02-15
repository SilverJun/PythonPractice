#
# Date : 2018.11.15 thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 딕셔너리 활용 프로그램
#

# 튜플의 키를 반환하는 함수를 통해 정렬.
def returnKey(tup):
    return tup[0]

gradeCounts = { 'A':8, 'D':3, 'B':15, 'F':2, 'C':6, 'P':7, 'I':1 }

# 1
print("All the keys")
for key in gradeCounts:     # 키 출력 반복문
    print(key)

# 2
print("All the values")
for key in gradeCounts:     
    print(gradeCounts[key])     # 키를 통해 값을 출력하는 반복문

# 3
print("All of the key and values pairs in key order")
orderList = list(gradeCounts.items())   # 리스트-튜플 형식으로 변환.
orderList.sort(key=returnKey)   # 키를 설정함으로써 정렬 가능해짐.
print(orderList)

# 4
print("The average value")
avg = 0.0
for i in orderList:
    avg += i[1]

avg /= len(orderList)       # 평균 구함.
print(avg)

# 5
for i in orderList:
    print(i[0]+":", "*"*i[1])       # *문자열을 값 만큼 곱해서 나타냄.

