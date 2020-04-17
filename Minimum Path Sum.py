"""
Explanation: Let us examine the first row and first column alone while we ignore other position in the grid for now.
First row: The sum of any chosen position (0,j) on the first row is strictly the sum of all other position to the left of it, (0,j) inclusive.
First column: The sum of any chosen position (i,0) on the first column is strictly the sum of all other position above it, (i,0) inclusive.
Since we know how to compute the sum for all the positions on the first row and first column, let us create a 2-dimensional array called Sum of grid size and use it to store the sum to get to each of these positions.
We can initialize all the first row(0,j) and the first column(i,0)of Sum as we've discussed
how to directly compute the sum at these positions above.
Main Logic: When we are at a particular position(i,j) where i or j is not zero i.e our
current position is not on the first row or column. There are only two previous positions
we are likely to have come from: (i,j-1) left or (i-1,j) up.
Since we care about the minimum sum, we must choose between positions (i,j-1) left or (i-1,j) up that has a minimum sum.
Therefore, Sum(i,j) = min(Sum(i-1,j),Sum(i,j-1)) + Sum(i,j)
We calculate Sum(i,j) for every positions in Sum starting from (1,1)
The value at the bottom right of the Sum array is our answer
"""
class Solution:
    def minPathSum(self, grid) -> int:
        if not grid: return 0
        nrow = len(grid)
        if not grid[0]: return 0
        ncol = len(grid[0])
        
        dp = [[0]*ncol for _ in range(nrow)]
        dp[0][0] = grid[0][0]
        #initialize all first column
        for i in range(1,nrow):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        #initialize all first row
        for j in range(1,ncol):
            dp[0][j] = dp[0][j-1]+grid[0][j] 
        for row in range(1,nrow):
            for col in range(1,ncol):
                dp[row][col] = grid[row][col] + min(dp[row-1][col],dp[row][col-1])
         
        return dp[-1][-1]
test = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(test))


