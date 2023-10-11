'''
    작성일: 2023년 10월 11일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: lAB 6-4 리스트엣 최대값, 최소값을 찾아 돌려주는 함수,

    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력받아 최대, 최소값을 찾아 돌려주는 함수

'''
import random

def m(first):
    n=min(first)
    x=max(first)
    return n,x

while True:

    first=[]

    for i in range(10):
        first.append(random.randint(10,99))

    MIN,MAX=m(first)

    print("생성된 리스트 : ",first)

    choice=input("최소값과 최대값 중 무엇을 찾으시겠습니까(min or max)?")

    if choice=='min':
        print(f"최소값은 {MIN}입니다")
    elif choice=='max':
        print(f"최댓값은 {MAX}입니다")


