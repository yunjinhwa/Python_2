'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학과 202395022 윤진환
    터틀 그래픽으로 N각형 도형을 그려보자
    사용자로부터 그리고 싶은 도형의 변의 수를 입력받아
    도형을 그린다
'''

import turtle as t
t.shape("turtle")

#펜 자국 안남음
for i in range(5):
    t.penup()
    t.goto(-50,-50)
    t.pendown()

    num = int(t.textinput("도형그리기","몇각형의 도형을 그릴까요?"))

    for i in range(num):
        t.forward(100)  #길이
        t.left(360/num)
        
t.done()


