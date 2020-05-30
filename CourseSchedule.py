from collections import defaultdict
def canFinish(numCourses, prerequisites) -> bool:
    graph = defaultdict(set)
    for a,b in prerequisites:
        graph[b].add(a) 
    visited = [False]*numCourses 
    def dfs(vertex, parents): 
        if visited[vertex]:
            return True
        visited[vertex] = True
        returnVal = True
        for each in graph[vertex]:
            parents.add(vertex) 
            if each in parents:
                returnVal = False
            returnVal = dfs(each, parents) and returnVal
            parents.remove(vertex)
        return returnVal

    ans = True
    for i in range(numCourses):
        ans = ans and dfs(i, set())
    return ans
            
    
numCourses = 7
prerequisites = [[1,0],[2,1],[3,2],[4,3],[5,4],[6,5],[6,4],[5,0],[5,1],[5,2],[4,0],[4,1],[4,2],[6,4],[1,3]]

print(canFinish(numCourses, prerequisites))
