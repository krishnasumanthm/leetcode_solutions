# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        elif root.left is None:
            result = self.pathSum(root.right, sum-root.val)
            return [[root.val] + i for i in result]
        elif root.right is None:
            result = self.pathSum(root.left, sum-root.val)
            return [[root.val] + i for i in result]
        else:
            result = self.pathSum(root.left, sum-root.val)
            result.extend(self.pathSum(root.right, sum-root.val))
            return [[root.val] + i for i in result]
            