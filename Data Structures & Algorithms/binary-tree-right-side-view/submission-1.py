# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans =[]
        q = deque([root])
        while q:
            ans.append(q[-1].val)
            print(ans)
            for _ in range(len(q)):
                for a in q: print("q check:",a.val, end=" ")
                print()
                cur = q.popleft()
                print("popped: ", cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                for a in q: print("q check 2:",a.val, end=" ")
                print()
                
            
            
        return (ans)
                
        