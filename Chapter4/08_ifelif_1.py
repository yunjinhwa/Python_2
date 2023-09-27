'''
    작성일: 2023년 9월 27일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 점수를 입력받아 학점을 출력하시오.
        90~100: A학점
        80~89: B학점
        70~79: C학점
        60~69: D학점
        0~59: F학점
'''

score=int(input("점수를 입력하세요: "))

#논리 오류 발생

print("첫번째 성적 처리")

if score>=90:
    print("A학점")
elif score>=80:
    print("B학점")
elif score>=70:
    print("C학점")
elif score>=60:
    print("D학점")
else:
    print("F학점")


#저왁한 범위를 지정하자. -성적의 범위를 벗어나면 잘못된 점수 입력입니다.

print("두번째 성적 처리")

if 100>=score>=90:
    print("A학점")
elif 89>=score>=80:
    print("B학점")
elif 79>=score>=70:
    print("C학점")
elif 69>=score>=60:
    print("D학점")
elif 59>=score>=0:
    print("F학점")
else:
    print("잘못된 점수 입력입니다.")


print("세번째 성적 처리")

if 100>=score>=0:
    if score>=90:
        print("A학점")
    elif score>=80:
        print("B학점")
    elif score>=70:
        print("C학점")
    elif score>=60:
        print("D학점")
    else:
        print("F학점")
else:
    print("점수를 잘못 입력하셨습니다.")