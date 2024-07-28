# Same Tree/相同的树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q != None) or (p != None and q == None ): 
            return False
        elif p == None and q == None:
            return True
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    O(n) time, O(n) space



# 书写更简洁
class Solution_opt:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:                   # O(min(len(p), len(q))) time, O(min(len(p), len(q))) space (same)
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)