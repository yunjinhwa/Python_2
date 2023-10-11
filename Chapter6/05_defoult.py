'''
    작성일: 2023년 10월 11일
    작성자: 컴퓨터공학과 202395022 윤진환
    설명: 함수의 디폴트 인자
'''

def order(sum,pickle,onion):
    print("햄버거{}개-피클{},양파{}".format(sum,pickle,onion))



def order2(sum,pickle='기본',onion='기본'):
    print("햄버거{}개-피클{},양파{}".format(sum,pickle,onion))

order2(1,pickle ='뺌',onion='기본')