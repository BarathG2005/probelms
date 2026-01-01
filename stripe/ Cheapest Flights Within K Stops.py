class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))
        d =[float('inf')]*n
        d[src] = 0
        q = []
        heapq.heappush(q,(0,0,src))
        while q:
            t,w,node = heapq.heappop(q)
            if t>k:
                continue
            # if node == dst:
            #     return w 
            for v,val in adj[node]:
                if val+w<d[v]:
                    d[v] = val+w
                    heapq.heappush(q,(t+1,d[v],v))
        return d[dst] if d[dst]!=float('inf') else -1