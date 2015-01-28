# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return None
        stack = [root.right,root.left]
        temp = root
        while len(stack) != 0:
            current = stack.pop()
            if current is None:
                continue
            else:
                temp.left = None
                temp.right = current
                temp = temp.right
                stack.append(current.right)
                stack.append(current.left)
        return root
        