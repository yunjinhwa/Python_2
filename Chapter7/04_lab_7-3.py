'''
    작성일: 2023년 10월 18일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 도시의 인구 자료에 대한 슬라이싱하기.
'''
population=['seoul',9765,'busan',3441,'incheon',2954]

print("서울 인구: ",population[1]) #서울 인구만 슬라이싱해서 출력
print("인천 인구: ",population[-1]) #인천 인구만 슬라이싱해서 출력
print("도시 리스트: ",population[::2]) #도시만 슬라이싱해서 출력
print("인구의 합: ",sum(population[1::2])) #인구만 슬라이싱해서 함 구하고 출력



