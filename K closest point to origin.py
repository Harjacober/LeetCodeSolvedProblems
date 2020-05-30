from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        func = lambda x: x[0]**2 + x[1]**2
        points.sort(key=func)
        return points[0:K]
        
