# -*- coding: utf-8 -*-
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while A.count(elem) != 0:
            A.remove(A[A.index(elem)])
        return len(A)