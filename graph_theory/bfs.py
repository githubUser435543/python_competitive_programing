from collections import deque

def bfs(g):
    visted = [0 for n in g]
    q = deque()
    q.append(0) 
    visted[0] = 1
    while len(q) > 0:
        curr = q.popleft()
        print(curr)
        for e in g[curr]:
            if visted[e]: continue
            visted[e] = 1
            q.append(e)



