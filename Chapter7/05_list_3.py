'''
    작성일: 2023년 10월 18일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 리스트의 객체 생성과 참조
'''

fruits=["망고","멜론","리치"]

#실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사된다.
fruits2 = fruits

print("fruits",fruits)
print("fruits2",fruits2)
print()

fruits2[1] = "복숭아" #fruits2의 1번지 과일을 복숭아로 바꾼다

print("fruits",fruits)
print("fruits2",fruits2)
print()

#주소 확인 => 메모리 위치정보 알아보기 id()함수
print("fruits의 id", id(fruits))
print("fruits2의 id", id(fruits2)) #두 리스트의 id 정보가 같다
print()


'''
    리스트 내용 복제하기 list()함수
'''

fruits2 = list(fruits) #내용 복제

print("::내용 복제 후 1::")
print("fruits",fruits,id(fruits))
print("fruits2",fruits2,id(fruits2))
print()

#내용 복제 2

fruits3 = fruits[:]
print("::내용 복제 후 2::")
print("fruits",fruits,id(fruits))
print("fruits2",fruits2,id(fruits2))
print("fruits3",fruits3,id(fruits3))
print()

fruits3[0] = "멜론"
print("fruits",fruits)
print("fruits3",fruits3)
print()



