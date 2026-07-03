# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pre(res,root):
            if not root: return
            print(root.val)

            res.append(root.val)
            pre(res,root.left)
            pre(res,root.right)
        pre(res,root)
        return res