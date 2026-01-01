def comopute_penalty(c, ct):
    y = c.count("Y")
    n = 0
    ans = 0
    mi = float("inf")
    for i in range(ct):
        if c[i] == "Y":
            y -= 1
        else:
            n += 1
    return y + n


def min_time(c):
    l = len(c)
    y = c.count("Y")
    if y == l:
        return l
    n = 0
    ans = 0
    mi = float("inf")
    for i in range(l):
        if y + n < mi:
            mi = y + n
            ans = i
        if c[i] == "Y":
            y -= 1
        else:
            n += 1
    if y + n < mi:
        mi = y + n
        ans = l
    return ans


def getAllClosing(log):
    tokens = log.split()
    st = []
    res = []

    for t in tokens:
        if t == "BEGIN":
            st.append("")
        elif t == "END":
            c = st.pop()
            res.append(min_time(c))
        else:
            st[-1] += t

    return res
