def valid():
    st=input()
    stack1=[]
    open_close={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in st:
        if c in open_close:
            if stack1 and stack1[-1]==open_close[c]:
                stack1.pop()
            else:
                return False
        else:
            stack1.append(c)
    return True if not stack1 else False
    

print(valid())