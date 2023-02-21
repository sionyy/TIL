until = int(input())

def down(level):
    print(level,end='')
    if level==until:
        return
    else:
        [down(level+1) for _ in range(until)]


print(down(0))