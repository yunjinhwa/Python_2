'''
    작성일: 2023년 10월 4일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: while문과 turtle문을 사용하여 별을 그려라
'''

import turtle as t
t.shape("turtle")

i=0
while i < 5:
    t.forward(300)
    t.right(144)
    i += 1

t.done()