#
# Date : 2018.12.06 thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 머지소트 구현 프로그램.
#

def mergeSort(list1, list2):
    rlist = list1 + list2       # 리스트 병합
    rlist.sort()        # 정렬

    count = 0
    i = 0
    while i < len(rlist):       # 중복되는 값들을 없애기 위해서 반복문
        j = i + 1
        while j < len(rlist):   # 해당 원소와 비교해 2개이상 같은 값이 나오면 삭제해야함.
            if rlist[i] == rlist[j]:
                count+=1
                if count > 1:
                    rlist.pop(j)    # 삭제
                    j-=1
            j+=1

        count = 0
        i+=1
    
    return rlist

