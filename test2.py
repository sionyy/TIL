N=int(input())

def run(x):
    arr=[[0]*3 for _ in range(3)]
    if x <10:
        for i in range(3):
            for j in range(3):
                for k in range(1,10):
                    arr[i][j] = k