def remove_element():
    inp=list(map(int,input().split()))
    value=int(input())
    i=len(inp)-1
    while i>=0:
        if value==inp[i]:
            inp.remove(inp[i])
        i-=1
    print(len(inp),inp)

remove_element()
