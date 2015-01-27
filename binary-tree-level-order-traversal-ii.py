# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        result = []
        level = [root]
        while len(level) != 0:
            result.append(level)
            level = []
            for node in result[-1]:
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
        result = [[node.val for node in level] for level in result]
        
        return result [::-1]