'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학과 202395022 윤진환
    설명 : turtle 모듈 활용하기
'''
import turtle as t # 터틀 모듈을 사용하기 위한 준비(turtle 클래스 객체를 t로 생성)

t.shape('turtle')
t.speed(2)

#선 그리기
#t.forward(200) #200픽셀 이동

#삼각형 그리기
"""
t.forward(200)# 200픽셀 이동
t.left(120) #왼쪽으로 120도 회전
t.forward(200)# 200픽셀 이동
t.left(120) #왼쪽으로 120도 회전
t.forward(200)# 200픽셀 이동
"""

for i in range(5):
    t.forward(100)# 200픽셀 이동
    t.left(144) #왼쪽으로 120도 회전




t.mainloop() #그림판 유지

