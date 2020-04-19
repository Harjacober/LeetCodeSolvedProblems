# Approach 1
class BinarySearchUsingPeak:
    def search(self,arr,target):
        def findPeak(arr):
            n=len(arr)
            left,right = 0,n-1
            while right-left>1:
                mid = (left+right)//2
                if arr[mid]>arr[right]:
                    left = mid
                else:
                    right = mid
            l = left if arr[left]<arr[right] else right
            return l,(l-1)%n
        def helper(arr,left,right,target):
            n = len(arr)
            mid = n//2
            count = 1
            while mid>=0 and count>0: 
                pivot_pos = (left+((right-left)%n)//2)%n
                if target<arr[pivot_pos]:
                    right = (pivot_pos)%n
                elif target > arr[pivot_pos]:
                    left = (pivot_pos+1)%n
                else:
                    return pivot_pos
                if mid==0: count -= 1 
                mid = mid//2
            return -1
        left,right = findPeak(arr) 
        return helper(arr,left,right,target)

#Approach two (Modifying existing binary search algorithm
"""
Note: At any chosen position in the array, either the left or right part of the array is
strictly increasing.
Given that we want to apply the binary search algorithm, we choose the midpoint of the array as out initial position and check whether the left or right part is strictly increasing.
The left part of the array is strictly increasing if the elememnt at array[midpoint]>= array[0]. Otherwise, the right part is strictly increasing.
If the left part is strictly increasing, we search it, if and only if target>=array[0] and target<array[midpoint], else the target can't be found here, we then search the right part
If the right part is strictly increasing, we search it if and only istarget>array[midpoint] and target<=array[lastpos]
We immediately return the postion when target==arr[midpoint]
"""
class BinarySearchPlus:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        low,high = 0,len(nums)-1
        while low<high:
            mid = low + (high-low)//2
            if target==nums[mid]: return mid
            #The left half is strictly increasing
            if nums[low] <= nums[mid]:
                #The target is in the left half
                if target>=nums[low] and target<nums[mid]:
                    high = mid-1
                else:
                    #target is in the right half
                    low = mid+1
            else: #The right half is strictly increasing
                #Target is in the right half:
                if target>nums[mid] and target<=nums[high]:
                    low=mid+1
                else:
                    #target is in the left half
                    high = mid-1
        return low if nums[low]==target else -1
        
                
 


    
