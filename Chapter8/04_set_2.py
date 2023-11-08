'''
    작성일: 2023년 11월 8일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 집합의 연산
'''

#비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}
print("num1 == num2 ?",num1 == num2)

#6개의 숫자로 집합 생성
num_set = {4,6,7,8,3,6}
print("num_set: ",num_set)
print("num_set의 길이: ",len(num_set))
print("num_set 중 가장 큰 값: ",max(num_set))
print("num_set 중 가장 작은 값: ",min(num_set))
print("num_set 합계: ",sum(num_set))

num1 = {1,2,3}
num2 = {3,4,5}

#합집합
print("num1 | num2: ",num1 | num2) #합집합 연산자 |
print("num1.union(num2): ",num1.union(num2)) #합집합 메소드 .union()
print("num1 & num2: ",num1&num2) #교집합 연산자 &
print("num1.intersection(num2): ",num1.intersection(num2)) #교집합 메소드 .intersection()
print("num1-num2: ",num1-num2) #차집합 연산자 -
print("num1.difference(num2): ",num1.difference(num2)) #차집합 메소드 .difference()
print("num1 ^ num2: ",num1 ^ num2) #대칭차집합 연산자 ^
print("num1.symmetric_difference(num2): ",num1.symmetric_difference(num2)) #대칭차잡합 메소드 .symmetric_difference




