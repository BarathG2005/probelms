class Solution:
    def calcEquation(self, s: List[List[str]], values: List[float], q: List[List[str]]) -> List[float]:


        n = len(s)
        adj = defaultdict(list)
        for i in range(n):
            adj[s[i][0]].append((s[i][1],values[i]))
            adj[s[i][1]].append((s[i][0],1/values[i]))
        def bfs(a,b):
            vis = set()
            vis.add(a)
            q = deque()
            q.append((a,1.0))
            if a not in adj or b not in adj:
                return -1.0
            while q:
                n,w = q.popleft()

                if n == b:
                    return w
                for v,ww in adj[n]:
                    if v not in vis:
                        q.append((v,ww*w))
                        vis.add(v)
            return -1
        def dfs(a,b,vis):
            if a not in adj or b not in adj:
                return -1.0
            if a==b:
                return 1.0
            vis.add(a)
            for v,w in adj[a]:
                if v not in vis:
                    r = dfs(v,b,vis)
                    if r!=-1.0:
                        return r*w
            return -1.0

        ans = []
        
        for i in range(len(q)):
            ans.append(dfs(q[i][0],q[i][1],set()))
        return ans


        