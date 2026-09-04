# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root or not subroot:return False
        def check(r,s):#check equality 
            if not r and not s:return True
            if r and s and r.val==s.val:
                return ((check(r.left,s.left)and
                check(r.right,s.right)))
            else:
                return False
        if root.val==subroot.val and check(root,subroot): return True
        return (self.isSubtree(root.left,subroot)or
            self.isSubtree(root.right,subroot))