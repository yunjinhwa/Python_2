'''
    작성일: 2023년 10월 18일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 입력을 받아 맛있는 과일의 리스트를 만들자.

    좋아하는 과일 5개를 입력받아 리스트에 저장한다.

    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단한다.
'''

fruits=[]

for i in range(5):
    fruits.append(input(str(i+1) + ". 좋아하는 과일을 입력하세요: "))

print()
find_fruit = input("찾으려는 과일을 입력하세요: ")
print()

if find_fruit in fruits:
    print(find_fruit,"은(는) 당신이 좋아하는 과일입니다.")
    print()
else:
    print(find_fruit,"은(는) 당신이 좋아하지 않는 과일입니다.")
    print()




