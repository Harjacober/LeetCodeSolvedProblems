"""
Explanation: One or more adjascently conected "1"s represents an Island
Intuition: For every single postion(i,j)such that grid(i,j)=="1", find all adjascently connected "1"s linked to that position and group them as a single Island.
We can find all adjascently connetcted "1"s to grid(i,j)="1" using DFS.
Note: we cannot visit the same position twice. That is, a "1"that makes up a particular Island, can never be a part of another Island.
Thus, we can apply several strategy to keep track of the position we've visited.
    strategy one: Initialize a boolean array of grid size to false and set visited position to True
    strategy two: use the same grid array and change the value of "1"at visited position to "0" since we will only visit where grid(i,j)=="1"
We then iterate through all position in the grid and call DFS at each position if an only if grid(i,j)=="1". We then use a count variable to keep track of the number of Island. we will increment count as long as the current position (i,j)we are, grid(i,j)== "1".
Implementation of DFS: Consider a position(i,j), there are only at most four possible positions adjascent to(i,j).
    grid(i+1,j) if i+1<len(gridrow)
    grid(i-1,j) if i-1>=0
    grid(i,j+1) if j+1<len(gridcol)
    grid(i,j-1) if j-1>=0
Time Complexity:O(n^2)as we only visit each cell in the grid once
Space Complexity: O(4^n) recursion stack
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,grid):
            if grid[i][j]=="0": return 0
            
            grid[i][j]="0"
            dfs(i,j-1,grid) if j-1>=0 else 0
            dfs(i,j+1,grid) if j+1<len(grid[0]) else 0
            dfs(i-1,j,grid) if i-1>=0 else 0
            dfs(i+1,j,grid) if i+1<len(grid) else 0
            
        
        count=0
        nrow=len(grid)
        if nrow==0: return 0
        ncol=len(grid[0])
        if ncol==0: return 0
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j,grid)
                        
                        
        return count
