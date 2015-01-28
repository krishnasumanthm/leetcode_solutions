# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        level = [root]
        i = 1
        while len(level) != 0:
            result.append(level)
            temp = result[-1]
            temp = temp[::-1]
            level = []
            if i%2 ==1:
                for node in temp:
                    if node.right is not None:
                        level.append(node.right)
                    if node.left is not None:
                        level.append(node.left)
            else:
                for node in temp:
                    if node.left is not None:
                        level.append(node.left)
                    if node.right is not None:
                        level.append(node.right)
            i += 1
        result = [[node.val for node in level]for level in result]
            
        return result