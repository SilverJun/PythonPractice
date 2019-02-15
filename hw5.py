#
# Date : 2018.11.05 Mon
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 피보나치 함수와 리스트에 해당 문자열이 어느 인덱스에 나오는지 확인하는 함수를 구현.
#

def fibo(n):
    fiboList=[1, 1] # 피보나치 리스트에 기본으로 1을 두개 넣음.
    for i in range(n-2): # 1이 두개 들어있으므로 n-2를 하고 구함.
        fiboList.append(fiboList[i] + fiboList[i+1])    # 피보나치 수를 구해서 append함.
    for i in range(n):
        print(fiboList[i], end='\t')    # 피보나치를 다 구하고 출력.

def N_find(listname, string):
    idxList = []
    cnt = 0
    for i in listname:  # 리스트에서 문자열 탐색
        if i.find(string) != -1:
            idxList.append(cnt)     # 존재하면 해당 인덱스를 넣는다.
        cnt += 1

    if len(idxList) != 0:   # 리스트가 비어있지 않다면 리스트를 반환
        return idxList
    else:
        return -1   # 리스트가 비어 있다면 -1을 반환.

# testCase
# fibo(7)
# print("")
# fibo(15)
# print("")

# fr = [ "apple", "banana", "lime", "blueberry", "strawberry"]
# print(N_find(fr, "a"))

# print(N_find(fr, "v"))

# print(N_find(fr, "berry"))

score = ['ahn', 60, 'cho', 90, 'park', 20]

N_find (score, 'a')