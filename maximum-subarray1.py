class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        current_max = A[0]
        max_val = A[0]
        for i in xrange(1,len(A)):
             current_max = max(A[i], current_max + A[i])
             max_val = max(max_val, current_max)
        return max_val