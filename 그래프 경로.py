# V,E : V노드개수 E개간선[아래]
# S,G : 출발 / 도착
V,E = map(int, input().split())

for i in range(E):
    S,G = map(int,input().split())

"""
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6

7 4
1 6
2 3
2 6
3 5
2 5

9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
"""
