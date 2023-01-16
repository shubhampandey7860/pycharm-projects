opr=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def postfix(expression):
    stack=[]
    output = ''

    for char in expression:
        if char not in opr:
            output +=char
        elif char=='(':
            stack.append('(')
        elif char==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[char]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(char)
    while stack:
        output+=stack.pop()
    return output
expression=input('Enter infix expression:')
print('postfix expression',postfix(expression))



