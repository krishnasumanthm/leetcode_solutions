# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        q = [[root,1]]
        result = 0
        while len(q) != 0:
            node, dep = q.pop(0)
            result = max(result, dep)
            if node.left is not None:
                q.append([node.left, dep+1])
            if node.right is not None:
                q.append([node.right, dep+1])
        return result