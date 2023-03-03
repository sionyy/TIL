H,W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
ans = [['']*W for _ in range(H)]
print(ans)
for i in range(H):
      for j in range(W):
            if arr[i][j]=='c':
                  pass


print(ans)
for i in range(H):
      print(*ans[i])