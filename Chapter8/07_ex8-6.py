'''
    작성일: 2023년 11월 8일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 심화문제 8-6
'''

student_tuple = [("211101",'강이안','010-123-1111'),('211102',"박동민",'010-123-2222'),('211103','김수정','010-123-3333')]

student={}

for number,name,phone in student_tuple:
    student[number] = [name,phone]

for key, value in student.items():
    print(key + " : ",value[0])

number = input("학번을 입력하시오: ")
print(number + "학생은" + student[number][0] + '이며 전화번호는' + student[number][1]+'입니다.')



        







