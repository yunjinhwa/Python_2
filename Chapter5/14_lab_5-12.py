'''
    작성일: 2023년 10월 4일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 더하기 암산 문제 만들기
          2개의 수로 더하기 결과를 맞추는 게임
          2개의 수는 1~100사이 랜덤으로 출제 됨
          사용자가 0을 입력하면 프로그램 종료
          즉 사용자가 0을 입력하기 전까지는 무한반복

    필요한 변수: num1, num2, answer
'''

import random #랜덤 묘듈 생성

print("-----암산게임 시작!-----")
while True: #무한반복
    num1=random.randrange(1,100) #랜덤 수 정하기
    num2=random.randrange(1,100) #랜덤 수 정하기
    print("{} 더하기 {} 는?".format(num1,num2),end='') #문제 출력
    answer=int(input()) #정답 입력받기
    if num1+num2==answer: #정답을 맞췄을 경우
        print("참 잘했어요!")
    elif answer==0: #0을 입력했을 경우
        print("게임을 종료합니다.")
        break #종료하기
    else: #오답을 입력 하였을 때
        print("정답은 {}입니다. 틀렸습니다.".format(num1+num2))

