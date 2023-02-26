"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        q = deque([root]) if root else None
        while q:
            level = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                level.append(node.val)
                for c in node.children:
                    q.append(c)
                    
            result.append(level)
            
        return result