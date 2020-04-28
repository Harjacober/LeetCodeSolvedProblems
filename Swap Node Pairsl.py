class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, val):
        self.root = ListNode(val)
    def insert(self, val):
        node = self.root
        self.inserthelper(node, val)
    def inserthelper(self, node, val):
        if node.next is None:
            node.next = ListNode(val)
        else:
            self.inserthelper(node.next, val)
    def printList(self):
        node = self.root
        self.printhelper(node)
    def printhelper(self, node):
        if node is not None:
            print(node.val, end=" -> ")
            self.printhelper(node.next)


class Solution: 
    def swapPairs(self, head:ListNode) -> ListNode:
        if head.next is None:
            return head 
        if head.next.next is not None:
            if head.next.next.next is not None:
                node = head.next.next
                head.next.next = self.swapPairs(node) 
        second = head.next #2-4-3
        temp = second.next #4-3
        head.next = temp #1-4-3
        second.next = head #2-1-4-3
        return second
ll = LinkedList(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
#ll.printList()
ll.printhelper(Solution().swapPairs(ll.root))
#ll.printList()
