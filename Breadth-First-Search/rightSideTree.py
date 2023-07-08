# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        if not root: 
            return []
        
        q = collections.deque([root])
        size =1 
        while q:
            rightSide = None 
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                 
            if rightSide:
                res.append(rightSide.val)


        return res
    
def build_tree(s):
    s = s[1:-1].split(',')
    if len(s) == 0:
        return
    nodes = [('root', s[0])]
    for i, c in enumerate(s[1:]):
        if c != 'null':
            if i & 1:
                nodes.append((nodes[i // 2][0] + '.right', c))
            else:
                nodes.append((nodes[i // 2][0] + '.left', c))
    for node in nodes:
        print(node[0] + ' = TreeNode(' + node[1] + ')')

# Call build_tree function by passing the input string
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
x = Solution().rightSideView(root)
print(x)