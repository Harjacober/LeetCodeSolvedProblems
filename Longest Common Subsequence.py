class Solution:
    #top down with memoization
    """
    We make use of two pointers i and j, we use i to move through text1 and j to
    move through text2. starting a index zero of both text, we move through the two
    strings, as we move, there are two scenarios, (1)text1[i] is equal to text2[j],
    we inrement both i and j by 1. (2) if text1[i] != text2[j], there are two possible
    moves to make, (i)increment i only or (ii)increment j only. the maximum of eithe
    of the two moves made should be chosen.
    """
    def recursiveLongestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(t1,t2,i,j,memo):
            if i==len(t1) or j==len(t2):
                return 0
            if memo[i][j]: return memo[i][j]
            if t1[i]==t2[j]:
                memo[i][j] = helper(t1,t2,i+1,j+1,memo) + 1
            else:
                memo[i][j] = max(helper(t1,t2,i+1,j,memo),helper(t1,t2,i,j+1,memo))
            return memo[i][j]
        memo = [[0]*len(text2) for _ in range(len(text1))]
        return helper(text1,text2,0,0,memo)
    
    # bottom up 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)] 
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]!=text2[j-1]:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]+1

        return dp[m][n]

text1 = "ghkabcdemsabkeg"
text2 = "fabkghnmskneg"
print(Solution().longestCommonSubsequence(text1, text2))
print(Solution().recursiveLongestCommonSubsequence(text1, text2))
