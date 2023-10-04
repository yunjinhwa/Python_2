'''
    작성일: 2023년 10월 4일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 반복을 제어하는 break, continue
         교재 137페이지

    Test word: Programming
    Pr
'''

word = input("단어를 입력하세요")

print("::break1::")
for i in word: #i에 word의 한 문자씩 입력
    if i=="a" or i == "e" or i =="i" or i == "o"  or i == "u": #만약 i의 값이 aeiou중 하나라면 반복 정지
        break #포함된 반복이 종료된다. 
    else: #아니면 줄바꿈 없이 출력
        print(i,end='')

print()

print("::break2::")
for i in word: #i에 word의 한 문자씩 입력
    if i in ["a",'e','i','o','u','A','E','I','O','U']: #만약 i의 값이 aeiou중 하나라면 반복 정지
        break #포함된 반복이 종료된다. 
    else: #아니면 줄바꿈 없이 출력
        print(i,end='')


print()


print("::continue::")
for i in word: #i에 word의 한 문자씩 입력
    if i in ["a",'e','i','o','u','A','E','I','O','U']: 
        continue #반복문 처음으로 돌아가라 => 반복할 문장을 어느정도 조정하기 위해 사용

    print(i,end='') #continue아래에 있으므로 모음은 출력하지 않는다
