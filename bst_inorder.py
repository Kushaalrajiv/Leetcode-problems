# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_order=[]
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     result_order.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return result_order
        stack=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
                
            curr=stack.pop()
            result_order.append(curr.val)
            curr=curr.right
        return result_order
