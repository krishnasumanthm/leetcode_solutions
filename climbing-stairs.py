# -*- coding: utf-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        i,j = 1,0
        for k in xrange(n+1):
            i,j = j, i + j
        return j
            

