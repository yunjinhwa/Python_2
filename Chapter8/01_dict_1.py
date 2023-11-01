'''
    작성일: 2023년 11월 1일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 8.1 키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}
'''
#빈 딕셔너리의 생성
phone_book1 = {}

#딕셔너리에 값 저장. key, value [key] = value
phone_book1['윤진환'] = "010-1234-5678"

print("phone_book1: ", phone_book1)

#딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {"홍길동" : "010-1234-5678"}

print("phone_book2: ",phone_book2)

phone_book3 = {}
phone_book3["윤진환"] = "010-1234-5678"
phone_book3["김현탁"] = "010-5678-1234"
phone_book3["한유진"] = "010-9876-1234"
phone_book3["박수연"] = "010-5432-5678"
phone_book3["김대영"] = "010-1000-5678"

print("phone_book3: ", phone_book3)

print()
print("::전화번호 phone_book3 출력::")
#모든 key 출력
print(phone_book3.keys())
#모든 value 출력
print(phone_book3.values())
#모든 key, value 출력
print(phone_book3.items())

print()
print("::전화번호 phone_book3 item 출력::")
for name,phone_num in phone_book3.items():
    print(name,":",phone_num)

print()

for key in phone_book3.keys():
    print(key, ":", phone_book3[key])

print()

print("딕셔너리 작성 시 :을 기준으로 key:value 작성")
person_dict = {"name" : "윤진환", "age" : 19, "class" : "1학년"}

print("name: ",person_dict["name"])
print("age: ",person_dict["age"])

print()

print("::정렬::")
#phone_book3를 정렬
#딕셔너리를 키를 기준으로 정렬하여 리스트로 변환
print(sorted(phone_book3))

print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)


print(":: 값을 기준으로 전체 정렬::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print()

print("::항목 삭제::")
del phone_book3["윤진환"]
print(phone_book3)

print("::전체 삭제::")
phone_book3.clear()
print(phone_book3)


