#
# Date : 2018.12.06 thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 파일 읽어서 내용 확인하는 프로그램
#
from tkinter import *
import sys

box = Entry(None)
box.pack()
label = Label(None, text = "input")
label.pack()

def isPalindrome(event) : 
    text = ""
    reverseText = ""
    curText = box.get()     # entry에 들어있는 문자열을 읽어들임.
    for i in range(len(curText)):
        if curText[i].isalpha():        # 알파벳이면
            text += curText[i].lower()  # 소문자로 바꿔서 텍스트에 붙인다.

    reverseText = text[::-1]        # 문자열 reverse.

    print(curText, text, reverseText)

    if text == reverseText:         # 문자열이 같으면
        label["text"] = "True"      # 라벨의 텍스트를 true로 변경
        print("True")
    else:
        label["text"] = "False"     # 아니면 라벨의 텍스트를 false로 변경
        print("False")
    
box.bind("<Return>", isPalindrome)      # 이벤트 핸들러 바인딩

mainloop()



    