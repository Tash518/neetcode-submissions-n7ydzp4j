# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        par = None
        while cur:
            par = cur
            if val<cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if val<par.val:
            par.left = TreeNode(val)
        else:
            par.right = TreeNode(val)
        return root