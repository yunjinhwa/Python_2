'''
    작성일: 2023년 10월 18일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 리스트 만들기
'''
#과일 리스트 만들기

fruits=['복숭아',"딸기","멜론"]
print("과일 목록: ",fruits)
print()

#수박 추가

fruits.append("수박")
print("과일 목록(수박 추가): ",fruits)
print()

fruits.append("망고")
print("과일 목록(망고 추가): ",fruits)
print()

#샤인머스켓 추가=> + 연산자 사용 : 연결연산자
fruits = fruits + ['리치']
print("과일 목록(리치 추가): ",fruits)
print()

num = [1,2,3] + [4,5,6]
print("숫자 리스트: ", num)
print()

# *연산자 => 반복횟수
num = [1,2,3] * 3
print("숫자리스트 * 3: ",num)
print()

#in 연산자 => 포함되어 있는가
print("과일 목록에 망고가 있나요?",'망고' in fruits)
print()

'''
    인덱스를 사용하여 리스트의 항목에 접근하기 178쪽
'''

#과일 리스트의 과일의 개수
print("과일 리스트의 과일의 개수는?",len(fruits))
print()

#과일 리스트 중 제일 첫번째 과일은?

print("과일 중 제일 좋아하는 과일은? ", fruits[0])
print()

print("과일 리스트 중 제일 마지막 과일은? ",fruits[-1]) # 음수 인덱스도 사용이 가능하나 순서는 리스트의 뒤에서 앞으로의 순서로 -1부터 시작
print()

#과일 중 가장 큰 과일은?
print("과일 중 가장 큰 과일은? (사전식 순서)",max(fruits))
print()
print("과일 중 가장 작은 과일은? (사전식 순서)",min(fruits))
print()

#정렬
fruits.sort() #오름차순
print("오름차순 정렬: ",fruits)
print()

fruits.sort(reverse=True) #내림차순
print("내림차순 정렬: ",fruits)
print()

'''
    리스트를 원하는 모양으로 자르는 슬라이싱
'''
print("과일 목록: ",fruits)
print()
print("과일 리스트 중 2,3,4번 과일은? ",fruits[1:4]) #1번지~4번지 앞까지
print()
print("과일 리스트 중 1~3번 과일은? ",fruits[0:3]) #0번지~3번지 앞까지
print()
print("과일 리스트 중 1~3번 과일은? ",fruits[:3])
print()
print("과일 리스트 중 3번 과일부터 마지막까지 과일은? ",fruits[2:])
print()
print("과일 리스트 중 1,2,5번 과일은?",fruits[::2])
print()
print('과일을 거꾸로 출력',fruits[::-1])
print()

'''
    리스트의 원소 값을 자유롭게 조작해 보자
'''

print("과일 목록: ",fruits)
print()

#원하는 위치에 두리안 추가 => insert() 메소드
fruits.insert(3,"두리안")

print("과일 목록: ",fruits)
print()

#위치 찾기 => index() 메소드

print("복숭아의 위치는?",fruits.index("복숭아"))
print()

#사과를 마지막에 추가
fruits.append("멜론")

print("과일 목록: ",fruits)
print()


#사과의 개수 => count() 메소드
print("멜론의 개수는? ",fruits.count("멜론"))
print()

'''
    리스트의 항목 삭제
'''

#멜론 삭제 => remove() 메소드 사용
fruits.remove("멜론") #처음 만나는 멜론만 삭제

print("과일 목록(멜론 삭제 후): ",fruits)
print()

#항목 삭제 => pop() 메소드
fruits.pop() #마지막 항목 삭제
print("과일 목록(마지막 과일 삭제): ",fruits)
print()

#del() => 키워드 => 딸기 삭제
del fruits[0]
print("과일 목록: ",fruits)
print()




