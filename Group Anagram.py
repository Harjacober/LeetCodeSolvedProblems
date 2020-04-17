from collections import defaultdict
def hashKey(string):
    arr = [0]*26
    for e in string:
        arr[ord(e)-97] += 1 
    return "".join(list(map(str, arr)))

def groupAnagrams(strs):
    dic = defaultdict(list)
    for each in strs:
        dic[hashKey(each)].append(each)
    ans = [dic[e] for e in dic]
    return ans

a = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(a))
