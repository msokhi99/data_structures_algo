# 100: 

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Solution: 
# Time Complexity: O(n).
# Space Complexity: O(n). 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
