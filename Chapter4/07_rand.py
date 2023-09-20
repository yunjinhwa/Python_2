'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학과 202395022 윤진환
    설명 : 선택문 if~else
           random 을 이용한 가위바위보 게임
'''

import random

print("-----가위바위보 시작!-----")
print("-------------------------")

player1=input("Player1의 이름:")
player2=input("Player2의 이름:")

num1=random.randrange(2)
num2=random.randrange(2)

print(player1, " : ",end="")

if  num1==0:
    print("가위")
elif num1==1:
    print("바위")
elif num1==2:
    print("보")

print(player2, " : ",end="")

if  num2==0:
    print("가위")
elif num2==1:
    print("바위")
elif num2==2:
    print("보")

if num1==num2:
    print("무승부!")
elif (num1==0 and num2==1) or (num1==1 and num2==0) or (num1==2 and num2==0):
    print(player2," 승!")
elif (num2==0 and num1==1) or (num2==1 and num1==0) or (num2==2 and num1==0):
    print(player1," 승!")

