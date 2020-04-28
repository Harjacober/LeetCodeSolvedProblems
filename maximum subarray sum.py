ans = [0]
kl = {}
def solution(k, nums, total, f, l, mem):
    if f > l:
        return
    if total == k:
        ans.append(l-f+1) 
    if str(f)+str(l) not in mem:
        mem[str(f)+str(l)] = True
        kl[str(f)+str(l)] = True
        solution(k,nums,total-nums[f],f+1,l,mem)
        solution(k,nums,total-nums[l],f,l-1,mem)

from collections import defaultdict,deque
def solution2(nums, k):
    dic = defaultdict(deque)
    summ = 0
    for i in range(len(nums)):
        summ += nums[i]
        dic[summ].appendleft(i+1) 
    cum = 0
    count = 0
    ans = [0]
    for j in range(len(nums)):
        search = k+cum
        if search in dic:
            if len(dic[search]) > 0:
                ans.append(dic[search][0]-count)
                dic[search].popleft()
        count += 1
        cum += nums[j] 
    return max(ans)
        

k = 1
nums = [1,-1]
total = sum(nums) 
solution(k,nums,total,0,len(nums)-1,{})
print(max(ans))
print(solution2(nums,k))
