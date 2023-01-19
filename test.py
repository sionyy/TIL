word=input()
num=len(word)//2    
if len(word)%2: 
    mid=word[num]  
else:
    mid=word[num-1:num+1]
print(mid)