# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.helper(a.left, b.right) and self.helper(a.right, b.left)

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     stack = [(root.left, root.right)]

    #     while stack:
    #         left, right = stack.pop()
    #         if not left and not right:
    #             continue
    #         if not left or not right:
    #             return False
    #         if left.val != right.val:
    #             return False
    #         stack.append((left.left, right.right))
    #         stack.append((left.right, right.left))

    #     return True
