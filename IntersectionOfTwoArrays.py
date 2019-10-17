from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        ans = []
        if nums1 < nums2:
            dic = Counter(nums1)
            nums1 = nums2
        else:
            dic = Counter(nums2)
            nums1 = nums1
        for i in nums1:
            if i in dic:
                if dic[i] > 0:
                    ans.append(i)
                    dic[i] -= 1 
                    
        return ans
    def sortedApproach(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        print(nums1,nums2)
        i = 0
        j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            print(i,j)
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans         
nums1= [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().sortedApproach(nums1,nums2))
