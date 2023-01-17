def su(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)

    print(sum)

s=input()
su(n)