data = list()
rst = list()

while True:
    a = input()
    if a == '.':
        break
    data.append(a)
    



for i in data:
    idx = 0
    stack = list()
    for j in i:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            try:
                parenthesis = stack.pop()
                if parenthesis == '[':
                    idx = 1
                    break
            except:
                idx = 1
                break

        elif j == ']':
            try:
                parenthesis = stack.pop()
                if parenthesis == '(':
                    idx = 1
                    break
            except:
                idx = 1
                break

    if idx == 1:
        rst.append("no")
    else:
        if len(stack) == 0:
            rst.append("yes")
        else:
            rst.append("no")
            
                
for r in rst:
    print(r)