from collections import defaultdict

def solution(N,dislikes):
    dic = defaultdict(set)
    for l,r in dislikes:
        dic[l].add(r)
        dic[r].add(l)
    partition = {}
    def dfs(node, g):
        if node in partition: 
            return partition[node] == g

        partition[node] = g
        return all(dfs(each, 1-g) for each in dic[node])

    return all(dfs(node, 0) for node in range(1,N+1) if node not in partition)
N = 4
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(solution(N,dislikes))
