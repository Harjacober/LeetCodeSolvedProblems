# Author: Jacob Audu
# Date Created: 01/05/2020
"""
**Explanation:** Let's begin by initializing `left=1` and `right=n`, we start from
the midvalue `mid=(left+right)//2` but it's safer to use `mid=left+(right-left)//2`
in order to avoid overflow.
We check if the midvalue is a bad version `isBadVersion(mid)==True`, if it is
`True`, then it is guaranteed that other later version will be `True` but there's
a chance that there are earlier bad versions, so we look to the left by setting
`right=mid`. if the midvalue is not a bad version i.e `isBadVersion(mid)==False`,
then we can only look to the right. we do this by setting `left=mid+1`.
We continue until `left<right`, once we are done, we simply return the current
value of  `right`.
```
"""
class Solution:
    def firstBadVersion(self, n): 
        l,r=1,n 
        while l<r:
            mid=l+(r-l)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        return r
