def exp(s):
    n = len(s)
    pre = ""
    suf = ""
    i =0
    while i<n and s[i]!="{":
        pre+=s[i]
        i+=1
    i+=1
    ans = []
    temp = ""
    while i<n :
        if s[i] == "," and temp!="": 
            ans.append(pre+temp)
            temp = ""
        elif s[i] == "}":
            ans.append(pre+temp)
            break
        else:
            temp+=s[i]
        i+=1
    if i>n-1:
        return ans 
    for k in range(len(ans)):
        ans[k] = ans[k]+s[i+1:]
    return ans

print(exp("/2022/{jan,feb,march}/report"))
print(exp("over{crowd,eager,bold,fond}ness"))










    
