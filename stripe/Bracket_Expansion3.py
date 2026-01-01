# leetcode 1096
class Solution:
    def braceExpansionII(self, s: str) -> List[str]:
        n = len(s)
        st = []
        cur = set([""])
        for i in s:
            if i == "{":
                st.append(cur)
                st.append("{")
                cur = set([""])
            elif i == "}":
                temp = cur
                while st[-1]!="{":
                    temp|=st.pop()
                st.pop()
                prev = st.pop() if st and st[-1]!="{" else set([""])
                new = set()
                for a in prev:
                    for b in temp:
                        new.add(a+b)
                cur = new
            elif i == ",":
                st.append(cur)
                cur = set([""])
            else:
                new = set()
                for r in cur:
                    new.add(r+i)
                cur = new
        return sorted(cur)