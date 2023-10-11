'''
    작성일: 2023년 10월 11일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: def 예약어를 이용하여 함수 작성하고 호출하기
'''


print("def 예약어를 이용하여 함수 작성하고 호출하기")


#함수 선언
def address():
    print("부산시 사상구")
    print("괘법동 산 1-1번지")
    print("신라대학교 국제 교육관 552호")

#함수 호출
address()
address()

print()

'''
    함수의값을 넘겨주고 일을시킨다
    인자와 매개변수
'''
print("인자와 매개변수")

#함수 선언
def welcome(name): #name은 매개변수
    print(name,"님 안녕하세요")


#함수 호출
welcome("윤진환")
welcome("홍길동")

