#
# Date : 2018.09.16
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 점수를 입력받아 알맞은 등급을 출력하는 프로그램.
#

score = float(input("Input your score : "))

gradeType = input("Input Letter(L) or PF(PF) : ")

print("Your grade is ", end = '')
if score > 90:
    if gradeType == "L":
        print("A")
    elif gradeType == "PF":
        print("PD")
elif score > 80:
    if gradeType == "L":
        print("B")
    elif gradeType == "PF":
        print("Pass")
elif score > 70:
    if gradeType == "L":
        print("C")
    elif gradeType == "PF":
        print("Pass")
elif score > 60:
    if gradeType == "L":
        print("D")
    elif gradeType == "PF":
        print("Pass")
else:
    if gradeType == "L":
        print("F")
    elif gradeType == "PF":
        print("Fail")

