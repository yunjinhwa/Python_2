'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학과 2020395022 윤진환
    설명 : 선택문 if
           성적을 입력 받아 60점 이상이면 "합격입니다."를 출력
'''

score=int(input("점수를 입력하시오"))

if score >= 60:
    print("합격입니다.")


'''
    자동차의 속도를 입력받아 속도를 출력하고,(현재 속도 : 00km/h)
    속도가 30km/h 이상이면
    "과속입니다. 속도를 줄이세요."를 출력하고,
    속도와 상관없이 "안전 운전하세요."출력
'''

speed=float(input("속도을 입력하시오(km/h) : "))

# print("현재 속도 : {}km/h" .format(speed))
print(f"현재 속도 : {speed}km/h") #따옴표 앞 f는 format의 f를 따와 사용

if speed >= 30:
    print("과속입니다. 속도를 줄이세요.")

print("안전 운전하세요.")


