MAP = [['A','B','G','K'],
       ['T','T','A','B'],
       ['A','C','C','D']]

# AB
# CD

pattern = list(map(str, input()))
pattern2 =list(map(str, input()))
all = pattern+pattern2

ny = [0,0,1,1]
nx = [0,1,0,1]


def check(y,x):
    result=[]
    for i in range(4):
        dy = y + ny[i]
        dx = x + nx[i]
        result.append(MAP[dy][dx])
    return result

count=0
for i in range(2):
    for j in range(3):
        if check(i,j) == all:
            count = count+1

if count > 0:
    print(f'발견({count}개)')
else:
    print('미발견')