"""
Approach 1: Binary Search
*Explanation:* Since each row of the matrix is sorted, we can do a binary search
on each row to find the position of the leftmost `1`
We modify the binary search algorithm in such a way we don't return once we find
a `1`, rather, we keep track of the minimum position of the `1s` we have seen so
far till we complete the binary search
We applyy the binary search on each row amd keep track of the minimum position only.
"""
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:
import sys
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def bsearch(bM,row,n):
            l,r=0,n-1
            best=sys.maxsize
            while l<=r:
                mid = l+(r-l)//2
                val = bM.get(row,mid)
                if val==1: 
                    best=min(best,mid)
                    r=mid-1
                else: l=mid+1
            return best
        best=sys.maxsize
        m,n=binaryMatrix.dimensions()
        for i in range(m):
            best=min(best,bsearch(binaryMatrix,i,n))
        return -1 if best==sys.maxsize else best
