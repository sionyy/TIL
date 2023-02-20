T = int(input())
for tc in range(1,T+1):
    st = input()
    box = []

    for i in range(len(st)):
        if st[i] == '{' or st[i] == '}' or st[i] == '(' or st[i] == ')':
            box.append(st[i])

    stack = []
    def check():
        for i in range(len(box)):
            if box[i] == '{' or box[i] == '(':
                stack.append(box[i])
            elif box[i] == '}' or box[i] == ')':
                if not stack:
                    return 0
                elif box[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif box[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif box[i] == ')' and stack.pop() == '{':
                    return 0
                elif box[i] == '}' and stack.pop() == '(':
                    return 0
            if i == len(box)-1:
                if len(stack)>0:
                    return 0
        return 1

    print(f'#{tc} {check()}')