#
# Date : 2018.12.06 thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 파일 읽어서 내용 확인하는 프로그램
#

def CountFile(filename):
    try:
        fp = open(filename, "r", encoding = 'UTF-8')    # 파일 열기.
    except IOError as err:
        print("I/O Error:", err)
        return
    
    fileContent = fp.readlines()        # 문자열 읽어 들이기.

    line = 0
    charSpace = 0
    char = 0
    word = 0

    for i in range(len(fileContent)):
        charSpace += len(fileContent[i])    # 공백포함 문자열 길이 구하기.
        for j in range(len(fileContent[i])):
            if fileContent[i][j] not in [' ', '\t', '\n']: # 공백문자가 아니면 갯수를 증가.
                char+=1
        word += len(fileContent[i].split())     # split해서 나온 단어 더하기.
    line = len(fileContent)

    print("line - ", line)
    print("character with space - ", charSpace)
    print("character - ", char)
    print("word - ", word)
    
CountFile("test.txt")

    