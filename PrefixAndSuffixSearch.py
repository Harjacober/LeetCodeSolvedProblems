class TrieNode:
    def __init__(self):
        self.isend = False
        self.children = [None]*26
        self.char = ''

    def put(self, char, node) -> None: 
        index = ord(char)-ord('a')
        self.children[index] = node
        self.children[index].char = char
    def containskey(self, char) -> bool:
        index = ord(char)-ord('a')
        return self.children[index] is not None
    def get(self, char):
        index = ord(char)-ord('a')
        return self.children[index]

class Trie:
    def __init__(self): 
        self.node = TrieNode()

    def insert(self, word) -> None: 
        node = self.node
        for char in word:
            if not node.containskey(char):
                node.put(char, TrieNode()) 
            node = node.get(char)
        node.isend = True
    def searchprefix(self, word):
        node = self.node
        for char in word:
            if node.containskey(char):
                node = node.get(char)
            else:
                return None
        return node

    def search(self, word):
        node = self.searchprefix(word)
        return node != None and node.isend
    
    def startswith(self, word):
        node = self.searchprefix(word)
        return node != None 
            
class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        self.weight = dict()
        self.ans = -1
        for i in range(len(words)):
            self.trie.insert(words[i])
            self.weight[words[i]] = i    
     
    def f(self, prefix: str, suffix: str) -> int:
        node = self.getnode(prefix) 
        self.dfs(node, prefix, suffix)
        return self.ans

    def getnode(self, prefix):
        node = self.trie.node
        prev = node
        for char in prefix:
            if node.containskey(char):
                prev = node
                node = node.get(char)
            else:
                return None
        return node    
                
    def dfs(self, node, prefix, suffix) -> bool:
        if node != None: 
            for each in node.children: 
                if each != None:  
                    prefix += each.char
                    if each.isend:
                        suff = prefix[-len(suffix)::]
                        print(prefix)
                        if suff == suffix:
                            self.ans = max(self.ans, self.weight[prefix]) 
                    if any(each.children):         
                        self.dfs(each, prefix, suffix)
                    else:
                        #i'm trying to backtrack here
                        prefix = prefix[0:len(prefix)-1]                               
                

words = ["jacob"]
wordFilter = WordFilter(words) 
print(wordFilter.f("j","ob"))

