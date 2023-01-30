#1000이하 2와 7의 배수를 모두 더하시오.

result = 0
for n in range(1, 1000):
    if n % 2 == 0 or n % 7 == 0:
        result = n+result
print(result)



'''
1. for문 이용
ans_lst = []
for i in range(1)


'''