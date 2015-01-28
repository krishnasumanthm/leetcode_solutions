# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def get_paths_num(self, root, path_numbers, num):
        if root.left is None and root.right is None:
            path_numbers.append(num + root.val)
        if root.left is not None:
            self.get_paths_num(root.left, path_numbers, (root.val+num)*10)
        if root.right is not None:
            self.get_paths_num(root.right, path_numbers, (root.val+num)*10)

    def sumNumbers(self, root):
        path_numbers = []
        if root is None:
            return 0
        else:
            self.get_paths_num(root, path_numbers, 0)
        result = 0
        for number in path_numbers: 
            result += number
        return result