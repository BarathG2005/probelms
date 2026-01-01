def validation(header , server):
    head = header.split(",")
    ans = []
    server = set(server)
    for i in head:
        if i in server:
            ans.append(i)
    return ans 


