# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)

        if not root:
            return []

        ans = []
        while queue:
            i=0
            not_added=True
            length=len(queue)
            while i<length:
                node =queue.popleft()
                if node:
                    if not_added:
                        ans.append(node.val)
                        not_added=False
                    queue.append(node.right)
                    queue.append(node.left)
                i+=1

        return ans