def prefix():
    strs=list(map(str,input().split()))
    if len(strs) == 0:
        return ""
    prefix=strs[0]
    for i in range(1,len(strs)):
        while strs[i].find(prefix)!=0:
            prefix=prefix[0:len(prefix)-1]
            if prefix=='':
                return ''
    return prefix
        
print(prefix())