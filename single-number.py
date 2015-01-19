class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for val in A:
            result = val ^ result
        return result
        