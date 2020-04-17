class Solution:
    def climbingstairs(self, n: int) -> int:
        pass

count = 0
def stairs(ans, target):
    global count
    if ans == target:
        count += 1
        return
    for i in range(1,3):
        ans += i
        if ans <= target:
            stairs(ans, target)
        ans -= i
    return count
        
        
print(stairs(0, 4))
print(count)

answers = []
def combination_sum(k, arr, ans, target, array_ans):
    global answers
    if ans == target: 
        answers.append(list(array_ans))
        return
    for i in range(k,len(arr)):
        ans += arr[i]
        array_ans.append(arr[i])
        if ans <= target:
            combination_sum(i, arr, ans, target, array_ans)
        ans -= arr[i]
        array_ans.pop()
    return answers


inp = [1,2,3]
tar = 4
print(combination_sum(0, inp, 0, tar, [])   )     
print(answers)    
