from heapq import *

def dijkstras(g, start, end):
    pq = []
    heappush(pq, (0, start))
    visited = [-1 for n in g]
    while (len(pq) > 0):
        cW , cN = heappop(pq)
        if visited[cN] != -1: continue
        visited[cN] = cW 
        if (cN == end): return cW 
        for eW, eN in g[cN]:
            if visited[eN] != -1: continue
            heappush(pq, (cW + eW, eN))
