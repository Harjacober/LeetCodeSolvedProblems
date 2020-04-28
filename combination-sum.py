class Node:
    def __init__(self, value,arr):
        self.value = value 
        self.children = arr
        pass

class MyTrie:
    def __init__(self,arr):
        self.root = Node(-1,arr)
        self.arr = list(arr)
        self.size = len(arr)

    def insert(self):
        node = self.root
        self.inserthelper(node,0) 
    def inserthelper(self, node, count):
        count += 1
        array = node.children
        if count%self.size != 0:
            for i in range(len(self.arr)):
                value = array[i] 
                array[i] = Node(value, list(self.arr))
        #print(array,count)    
        for each in array:  
            if count%self.size != 0:
                self.inserthelper(each, count)
    def printall(self):
        self.printhelper(self.root)
    def printhelper(self, node): 
        children = node.children
        for each in children:
            if isinstance(each, Node):
                print("\t\t\t\t  {}".format(each.value))
                print("\n\t\t\t\t ||\n")
                print("\t\t\t\t{}".format(each.children))
                self.printhelper(each)
            
        

cand = [1,2,3]
trie = MyTrie(cand)
trie.insert()
trie.printall()
 
            
            

    
