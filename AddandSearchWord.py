class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isend = False

    def put(self, char, node) -> None:
        index = ord(char)-ord('a')
        self.children[index] = node
    def get(self, char):
        index = ord(char)-ord('a')
        return self.children[index]
    def containskey(self, char) -> bool: 
        index = ord(char)-ord('a')
        return self.children[index] is not None
    
class WordDictionary:
    def __init__(self):
        self.node = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.node
        for char in word:
            if not node.containskey(char):
                node.put(char, TrieNode())
            node = node.get(char)
        node.isend = True    
            
    def searchtree(self,node, word: str) -> bool: 
        for i in range(len(word)):
            char = word[i]
            if char != '.':
                if node.containskey(char):
                    node = node.get(char)
                else:
                    return False
            else: 
                for each in node.children:
                    if each != None: 
                        if self.searchtree(each, word[i+1:len(word)]):
                            return True
                return False        
        return node.isend
    def search(self, word):
        root = self.node
        return self.searchtree(root, word)
word = "jacob"                                    
obj = WordDictionary()
obj.addWord("jacob")
print(obj.search("j...e"))   
        
