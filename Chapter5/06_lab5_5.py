'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학과 202395022 윤진환
    반복문으로 팩토리얼 구하기
'''

num = int(input("정수를 입력하시오: "))
pac=1

for i in range(1,num+1):
    pac=pac*i

print(num,"! 은 {}이다.".format(pac))


