#
# Date : 2018.09.30 Sun
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 입력받은 문자열에서 원하는 문자열을 찾아 수를 세고 대소를 바꿔서 출력하는 프로그램.
#

# 입력
string = input("Input a sentence : ")
keyword = input("Input a word for search : ")

# 문자열을 검색하기 위해 일방적으로 lower케이스로 맞춘z다.
count = 0
stringFind = string.lower()
keywordFind = keyword.lower()

idx = 0
idx = stringFind.find(keywordFind, idx)     # 키워드 검색.
while idx != -1:    # idx가 -1이 아니라면 찾았다는 의미로 반복조건.
    count += 1      # 카운트 증가.
    idx = stringFind.find(keywordFind, idx+len(keyword)) # 다시 검색. 이때는 idx를 증가시켜서 중복으로 검색되지 않도록 시작 idx값을 지정해준다.

# 카운트 출력.
print("A word ‘"+ keyword +"’ appears", count, "times in the sentence.")

i = 0
while i < len(string):      # 문자열의 끝까지 반복, 중간에 키워드 찾고 그 부분을 건너뛰기 위해 while사용.
    if keyword.lower() == string[i:i+len(keyword)].lower():     # keyword랑 slice된 string이랑 비교.
        print(keyword.upper(), end='')    # 대문자로 출력
        i += len(keyword)   # 찾은 키워드 길이만큼 인덱스를 증가시켜준다.
    else:
        print(string[i], end='')    #그냥 출력.
        i += 1  # 1증가.
