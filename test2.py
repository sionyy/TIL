# print(ord('A')) # 65
# print(ord('D')) # 68
# print(ord('Z')) # 90

a,b = input().split()
for j in range(4):
    for i in range(ord(b)-ord(a)+1):
        print(chr(ord(a)+i),end=' ')
    print()