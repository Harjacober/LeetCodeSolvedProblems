class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def printbst(node):
    if node is None: 
        return
    print(node.val)
    printbst(node.left) 
    printbst(node.right)
def setnodepointer(node,i):
    newnode = node
    while i > 0:
        newnode = newnode.right
        i -= 1
    return newnode
def clone(root):
    if root == None:
        return None
    newtree = TreeNode(root.val) 
    newtree.left = clone(root.left)
    newtree.right = clone(root.right)
    return newtree
    
def generatetrees(n):
    if n==1:
        return [TreeNode(n)]
    res = generatetrees(n-1) 
    ans = []
    for each in res: 
        nnode = TreeNode(n)
        nnode.left = each
        ans.append(nnode) 
        node = clone(each)
        newnode = node 
        i = 0
        while newnode: 
            if newnode.right is not None: 
                i += 1
                temp = newnode.right
                newnode.right = TreeNode(n)
                node.right.left = temp
                ans.append(node)
                node = clone(each)
                newnode = node
                newnode = setnodepointer(node, i) 
            else:
                newnode.right = TreeNode(n)
                ans.append(node)
                newnode = None 
    return ans     
                 
bst = generatetrees(5)
for e in bst:
    printbst(e)
    print("\n")
    
def permutations(n):
    if n==1:
        return [[1]]
    res = permutations(n-1) 
    perm = []
    for each in res:
        for i in range(len(each)+1):
            temp = list(each)
            temp.insert(i,n)
            perm.append(temp)
    return perm

def insert_to_tree(node, val):
    path = []
    if node.val < val:
        if node.right is None:
            node.right = TreeNode(val)
        else:
            insert_to_tree(node.right, val)
    else:
        if node.left is None:
            node.left = TreeNode(val)
        else:
            insert_to_tree(node.left, val)



def uniquebst(n):
    answer = []
    allpermutations = permutations(n)
    print(allpermutations) 
    for each in allpermutations: 
        tree = TreeNode(each[0])
        for i in range(1, len(each)):
            node = tree
            insert_to_tree(node, each[i])
        answer.append(tree)
        print(tree.val)
    return answer
#searchtrees = uniquebst(3)
#for each in searchtrees:
#    print("\n")
#    printbst(each)
#    print("\n")
