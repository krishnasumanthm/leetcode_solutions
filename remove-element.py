# -*- coding: utf-8 -*-
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        j=0
        i=0
        while (i<len(A)):
            if A[i]!=elem:
                A[j]=A[i]
                j = j+1
            i = i+1
        return j