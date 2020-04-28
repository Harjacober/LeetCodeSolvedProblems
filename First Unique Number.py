class FirstUnique:
    def __init__(self, nums):
        self.dic = dict()
        self.head = None
        self.node = None
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        #always return the head of the queue
        if self.head: return self.head.value
        else: return -1

    def add(self, value):  
        if value not in self.dic:
            #add to queue
            if not self.head:
                self.head = LinkedList(value)
                self.node = self.head 
            else:
                temp = self.node
                temp.next = LinkedList(value)
                temp.next.prev = temp
                self.node = temp.next 
            self.dic[value] = self.node
        else:
            if self.dic[value]:
                node = self.dic[value]
                #remove this node from the queue
                if self.head:
                    if self.head == node:
                        self.head = node.next
                    if node.next: 
                        node.next.prev = node.prev  
                    if node.prev:
                        node.prev.next = node.next 
                self.dic[value] = None


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

nums = [8]*50000
firstUnique = FirstUnique(nums)
print([firstUnique.showFirstUnique(), firstUnique.add(7),firstUnique.add(3), firstUnique.add(3), 
firstUnique.add(7), firstUnique.add(17),
firstUnique.showFirstUnique()])