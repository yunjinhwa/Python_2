'''
    작성일: 2023년 11월 1일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: LAB 7-6 도시의 이름과 인구를 튜플로 
'''


city_info = [('서울',9875),("부산, ",3441),("인천",2954), ("광주",1501), ('대전', 1531)] #리스트 생성

max_population = city_info[0][1] #변수 만들기
min_population = city_info[0][1]
total_population = 0

max_city = city_info[0][0] #변수 비워두기
min_city = city_info[0][0]

for city, population in city_info: #city가 city_info 안에 있을 경우 반복실행
    total_population += population #도시 개수 세기
    if city[1] > max_population: #만약 city가 max보다 클 경우
        max_population= population #max 변수를 변경
        max_city = city #max 변수를 city로 변경
    if city[1] < min_population: #만약 city가 min보다 작을 경우
        min_population = population #min 변수를 더 작은 것으로 변경
        min_city = city #min 변수를 city로 변경

print("최대인구: {}, 인구: {}천명".format(max_city, max_population))
print("최소인구: {}, 인구: {}천명".format(min_city, min_population))
print("g리스트 도시 평균 인구: {}천명".format(total_population / len(city_info)))

