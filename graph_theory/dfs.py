

def dfs(g):
    stack = [0]
    visited = [0 for i in g]
    visited[0] = True
    while len(stack) > 0:
        curr = stack.pop()
        visited[curr] = True
        print(curr)
        for e in g[curr]:
            if visited[e]: continue
            visited[e] = True
            stack.append(e)
