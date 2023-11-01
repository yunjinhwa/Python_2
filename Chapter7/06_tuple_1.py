'''
    작성일: 2023년 11월 1일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 한번 생성하면 그 값을 고칠 수 없는 자료형: 튜플
'''

#리스트 생성
color_list = ["red","skyblue","black","lemon"]

#튜플 생성
color = ("red","skyblue","black","lemon")

#튜플 출력
print("color: ",color)

#color에 purple 추가하기
#AttributeError: 'tuple' object has no attribute 'append'
#튜플은 추가, 삭제가 안된다.
#color.append("purple")

#인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print("color 튜플: ",color)
print("color 튜플 중 2,3,4번은?", color[1:4])
print("color 튜플 중 1,2,3번은?", color[0:3])
print("color 튜플 중 3~끝번은?", color[2:])
print("color 튜플 중 1,3,5번은?", color[::2])
print("color 튜플 거꾸로 출력", color[::-1])

#튜플 끼리의 결합=> + 연산자.반복 => * 연산자
color = color + color+ color+color+color+color+color
print("color 튜플: ",color)
print("color 튜플을 10번 반복: ", color * 10)


