'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학과 202395022 윤진환
    설명 : 선택문 if~else
           random 을 이용한 가위바위보 게임
'''

import random

print("-----가위바위보 시작!-----")
print("-------------------------")

user=input("가위/바위/보 중 하나를 선택하시오")

num=random.randrange(2)

if  num==0:
    com="가위"
elif num==1:
    com="바위"
elif num==2:
    com="보"

print("-------------------------")
print("----사용자 : {}----".format(user))
print("----컴퓨터 : {}----".format(com))
print("-------------------------")

if com==user:
    print("무승부!")
elif (com=="가위" and user=="바위") or (com=="보" and user=="가위") or (com=="바위" and user=="보"):
    print("user 승!")
elif (user=="가위" and com=="바위") or (user=="보" and com=="가위") or (user=="바위" and com=="보"):
    print("컴퓨터 승!")

