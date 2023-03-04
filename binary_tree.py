from collections import deque


class WalkTree:

    def in_order(self,node):
        if node == None:
            return
        self.in_order(node.left)
        print(node.val)
        self.in_order(node.right)

    
    def dfs(self, node):
        if node == None:
            return
        
        print(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    
    def post_order(self,node):
        
        if node == None:
            return
        
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)

    
    def bfs(self,root):
        q = deque([root])

        while len(q) > 0:
            node = q.popleft()
            print(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    
    def __init__(self,root):
        self.root = Treenode(root)

    def get_node(self):
        return self.root

tree = BinaryTree(1)
tree.root.left = Treenode(2)
tree.root.right = Treenode(3)
tree.root.left.left = Treenode(4)
tree.root.left.right = Treenode(5)
tree.root.right.left = Treenode(6)
tree.root.right.right = Treenode(7)

print(tree.get_node())

walk = WalkTree()

walk.in_order(tree.get_node())
walk.dfs(tree.get_node())
walk.post_order(tree.get_node())

walk.bfs(tree.get_node())

