#
# Date : 2018.09.16
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 반복문을 활용해 다양한 문제를 해결하는 프로그램.
#

### 1
result = 0
for i in range(3, 10000, 2):    # 3부터 2씩 더하면 무조건 홀수다.
    result = result + i

print("#1 ", result)
###

### 2
print("#2 ", end = '')
result = 0
for i in range(10, 26):     # 10 부터 25까지.
    result = result + i
    print(result, end = ' ')
print("")
###

### 3
print("#3 ", end = '')
for i in range(0, 21):
    print(3**i, end = ' ')  #3의 i승을 출력.
###

### 4
a = int(input("input a : "))
b = int(input("input b : "))
result = 0
cnt = 0
for i in range(a+1, b):     # a+1 부터 b-1까지.
    if i % 2 == 1:         # 2로 나눈 나머지가 1이면 홀수.
        result = result + i
        cnt = cnt + 1
result = result/cnt
print("#4 ", result)
###

### 5
num = input("input number : ")
result = 0
for i in num:               # 문자열로 받아서 iterate.
    if int(i) % 2 == 1:    # 2로 나눠서 나머지가 1이면 홀수이니 합함.
        result = result + int(i)

print("#5", result)
###

