a,b,c=map(str, input().split())

if a[-1].upper() == b[0].upper() and b[-1].upper() == c[0].upper():
  print('Pass')
else:
  print('Fail')