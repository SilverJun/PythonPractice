#
# Date : 2018.10.17 Wed
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 컴퓨터가 정한 숫자 4개를 맞추는 게임.
#
from copy import *

myList = []

for i in range(10):
    myList.append(int(input()))     # 10개 입력받음

print(myList)

# shift right
first = myList[9]       # 첫번째칸에 들어갈 마지막 값 저장.
shiftList = [first]     # 마지막 값을 첫번째로 저장해놓음
for i in range(0, 9):
    shiftList.append(myList[i]) # 첫번째 값부터 하나씩 마지막 값 전까지 집어넣음.
myList = shiftList

print("Shift Right -", myList)
#

# remove Two Element
removeList = myList
removeList.pop(5)   # 10에서 중간 인덱스 pop
removeList.pop(4)   # 9에서 중간 인덱스 pop

print("Remove two element -", removeList)
#

# Find Second Largest Number
SecondList = deepcopy(myList)
SecondList.sort()       # 정렬하면 맨 뒤에서 2번째 값이 두번째로 큰 값임.
print("Second Largest Number is", SecondList[len(myList)-2])
#

# Find Duplicate Number
for i in range(len(myList)):
    for j in range(i+1, len(myList)):       # 반복을 할때 검색하고자 하는 인덱스 보타 하나 윗 부터 끝까지 탐색하면서 찾으면 중복을 모두 찾을 수 있다. 
        if myList[i] == myList[j]:
            print("exist duplicate elements")
            print("value :", myList[i], "index :", i, ",", j)


