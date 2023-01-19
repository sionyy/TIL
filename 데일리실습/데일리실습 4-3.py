A = [1, 1, 3, 3, 0, 1, 1]

def solution(A):
  answer = [A[0]]
  for i in range(1,len(A)):
      if answer[len(answer)-1]==A[i]:
       continue
      answer.append(A[i])
  return answer

print(solution(A))