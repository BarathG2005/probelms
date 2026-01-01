
#part 2

def brace_exp(s):
    i = 0
    n = len(s)
    ans = [""]
    while i<n:
        if s[i] == "{":
            st = ""
            temp = []
            i+=1
            while i<n and s[i]!="}":
                if s[i] == ",":
                    temp.append(st)
                    st = ""
                else:
                    st+=s[i]
                i+=1
            if st!="":
                temp.append(st)
            new_ans = []
            for r in ans:
                for t in temp:
                    new_ans.append(r + t)

            ans = new_ans
            
                    
        else:
            new_ans = []
            for r in ans:
                new_ans.append(r + s[i])
            ans = new_ans
        i+=1
    return ans

print(brace_exp("a{b,c}de"))