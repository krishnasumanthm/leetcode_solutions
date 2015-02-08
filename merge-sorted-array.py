class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i = i-1
            else:
                A[k] = B[j]
                j = j-1
            k = k-1
        if j >=0:  
            A[:j+1] = B[:j+1]
        
        return A
            
        
        