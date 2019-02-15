#
# Date : 2018.09.04 Thu
# Author : 글로벌리더십학부 21800633 장은준
# Purpose : 초를 입력받아 시분초로 변환하는 프로그램
#

sec = int(input("시간을 초 단위로 입력하시오 : "))

sec_backup = sec    # 초를 백업해서 저장해둔다.

hour = int(sec/3600)    # 초를 3600으로 나눠 시간을 구함
sec = sec - hour*3600   # 구한 시간을 원래 있던 초에서 빼준다.
min = int(sec/60)       # 시간을 구하고 남은 초에 60을 나눠 분을 구함.
sec = sec - min*60      # 구한 분을 초에서 빼줘서 남은 초를 구한다.

print(sec_backup, "초는 ", hour, "시간", min, "분", sec, "초입니다")    #결과 출력,
