'''
    작성일: 2023년 10월 4일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 단을 입력 받아 해당 단의 구구단을 출력하시오
            교재 130페이지

    문제 분석: 입력받은 단 하나로 고정
              1부터 9까지만 계산

    필요한 변수: dan(단을 입력받아 저장할 변수)
                dan2(해당 단의 구구단의 값)
                i(반복횟수 계산 및 구구단의 값 구하기)
'''


dan=int(input("단을 입력하시오"))
i=1

while i<=9:
    dan2=dan
    dan2=dan2*i
    print("{} X {} = {}".format(dan,i,dan2))
    i += 1
    