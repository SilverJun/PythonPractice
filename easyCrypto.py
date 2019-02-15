#
# Date : 2018.11.15 thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 간단한 암호화 프로그램
#

def easyCrypto(string):
    newString = []
    for i in range(len(string)):
        asc = ord(string[i])    # 문자를 아스키코드로 변환.
        if asc % 2 == 1:        # 아스키를 2로 나눠 홀짝 구분.
            asc += 1
        else:
            asc -= 1
        newString.append(chr(asc))      # 아스키코드를 다시 문자로 바꿈.
    return "".join(newString)       # string에 join 메소드를 통해 리스트를 문자열로 변경

# print(easyCrypto("abc"))
# print(easyCrypto("Zoo"))
# print(easyCrypto("BAB"))