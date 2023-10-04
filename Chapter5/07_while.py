'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학과 202395022 윤진환
    설명 : 조건에 따라 반복하는 while문
'''

#while 조건식 : 세미콜론(:) 반드시 사용
#   들여쓰기로 반복하면서 할 일 작성

under_construction = True   #공사중, 변수에 True를 대입한 것

#True일 동안 계속 반복
while under_construction : 
    response = input("공사가 완료 되었습니까?")
    if response=="네":
        under_construction=False #공사 완료

print("루프 탈출")


