"""
Consider the ***Example:*** `nums = [1,2,3]` , `k=6`
let's sum all the elements in `nums`  cumulatively, we get `cum_sum = [1,3,6]`. 
At index 0, `cum_sum[0]=1`
At index 1, `cum_sum[1]=3`
At index 2, `cum_sum[2]=6` (we found the target and there happen to be only one subarray).
Consider this ***Example:*** `nums=[1,-1,2,-2,1,2,3]` and `k=6`.
let's sum all the elements in `nums`  cumulatively, we get `cum_sum = [1,0,2,0,1,3,6]`
***what did you notice?*** There are some previous subarray that summed up to `0`. What does this tell us? It means if we decide to add the subarrays that summed up to `0` to our initial subarray `[1,2,3]` that summed up to `6`, we will still get a target value of `6`. 
The valid subarray whose sum equals k are: `[1,2,3]`, `[2,-2,1,2,3]`, `[1,-1,2,-2,1,2,3]`. Thus the total number of valid subarray is equal to the number of times `0` appeared in `cum_sum` plus `1` which is `2+1=3` in this case.
**Now let's look a different scenario where** `cum_sum[i] != target`
***Example:*** `nums = [5,4,1,2,3]`, `k=6`
Let's find the cumulative sum like we did earlier. `cum_sum = [5,9,10,12,15]`. let's just assume we are at the last index where we have a cumulative sum of `15`. Now subtract the target `k=6` from `15`, we have `15-6=9`. As we can see from the `cum_sum` array, we have a cumulative sum of `9` at index `1`, that means if we exclude all subarray in `nums` from index `1` backwards i,e `[5,4]`, we will have an array that sums up to `k=6` i.e `[1,2,3]`.
Another ***Example*** for further clarification: `nums = [9,-9,5,4,1,2,3]`, `k=6`.  
.`cum_sum = [9,0,5,9,10,12,15]`. Let's assume we are the last index again where the cumulative sum is `15`. We do the same as above, `15-6 = 9`. If we look at the `cum_sum` array, we will notice that `9` appeared at index 3 and index 0. Thus if we exclude all the subarray in `nums` from index `3` backwards, we will be left with `[1,2,3]` which sums up to `k=6`. Also if we exclude all the subarray from index `0` backwards, we will be left with `[-9,5,4,1,2,3]` which also sums up to `k=6`. Thus the total number of valid subarray in this second scenario is equal to the number of times `cum_sum[curr_pos] - k` appears in the `cum_sum` array,
**Implementation:** 
- We use an `Dictionary` to store the occurences of cumulative sums at each position, and a `count` variable to store our answer
- For every position in the array, if the cumulative sum is not equal to the target `k`, we find the the difference between the cumulative sum and k, i.e`cum_sum[curr_pos] - k ` and we check the `Dictionary` for number of occurence of this difference and add it `count`. But if the cumulative sum is equal to k we check the number of occurence of `cum_sum[curr_pos] - k ` in the `Dictionary`, add one to it it before adding to `count`  Note that when `cum_sum[i]==k`, `cum_sum[i]-k` will always be `0`.

"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        summ,count=0,0
        for e in nums:
            summ+=e
            if summ==k: count+=1
            if summ-k in dic:
                count+=dic[summ-k]
            dic[summ]+=1
        return count
