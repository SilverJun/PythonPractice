#
# Date : 2018.10.17 Wed
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 컴퓨터가 정한 숫자 4개를 맞추는 게임.
#

import random

# 리스트를 인자로 받아 같은 숫자가 있는지 확인하는 함수
# 중복값이 있으면 False반환.
def check_list(listname):
    for i in range(4):
        for j in range(4):
            if i == j: continue     # 리스트에서 같은 element끼리 비교를 피하는 조건.
            elif listname[i] == listname[j]:
                return False
    return True


comList = random.sample(range(1, 10), 4)    # 컴퓨터 숫자 생성. sample을 사용하면 중복없이 선택가능.
#print(comList)

cnt = 0     # 몇번만에 했는지
strike = 0
ball = 0
inputList = [0, 0, 0, 0]    #유저가 입력할 리스트.

while strike != 4:  # 스트라이크가 4개 되었을때 루프 탈출.
    strike = 0
    ball = 0

    for i in range(4):      # 일단 4개를 입력받는다.
        inputList[i] = int(input("Input a Number : "))
    while not check_list(inputList):    # 이후에 중복체크를 해서 될때까지 입력받음.
        print("Duplicated number found")
        for i in range(4):
            inputList[i] = int(input("Input a Number : "))
    
    for i in range(4):
        for j in range(4):
            if comList[i] == inputList[j]:      # 컴퓨터의 숫자와 입력 숫자가 같을때
                if i == j:
                    strike += 1     # 인덱스가 같으면 스트라이크
                else:
                    ball += 1       # 인덱스가 다르면 볼.
    print(strike, "strike,", ball, "ball.")
    cnt += 1


print("You Win! on", cnt, "try..")




