#리스트 함수
a = [5, 2, 3, 1, 4]

print('a -', a)
a.append(10)      #마지막에 데이터 삽입
a.sort()          #오름차순
a.reverse()       #반대차순
a.insert(2,7)     #위치지정 추가
a.remove(10)      #지정삭제
a.pop()           #마지막 원소 꺼내오고, 마지막 삭제
a.count()         #지정 원소 개수

xx = [9,0]
a.extend(xx)      #연장