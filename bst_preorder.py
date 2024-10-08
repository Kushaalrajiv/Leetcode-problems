# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_order=[]
        # def preorder(root):
        #     if not root:
        #         return
        #     result_order.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        stack=[]
        curr=root
        while curr or stack:
            if curr:
                result_order.append(curr.val)
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()
            
        return result_order