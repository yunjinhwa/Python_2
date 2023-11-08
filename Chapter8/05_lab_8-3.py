'''
    작성일: 2023년 11월 8일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: lab 8-3
'''

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("파티A, B에 참석한 사람들: ",partyA.union(partyB))
print("파티에 모두 참석한 사람: ",partyA.intersection(partyB))
print("파티A, B에 중복없이 참석한 사람: ",partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람: ",partyA.difference(partyB))