# -*- coding: utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return len(A)
        else:
            flag = 0
            pre = A[0]
            for i in xrange(len(A)):   
                if A[i] != pre:
                    A[flag+1] = A[i]
                    flag = flag+1
                    pre = A[i]
        A = A[0:flag+1]
        return len(A)

