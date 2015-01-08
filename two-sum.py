# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 17:43:23 2015

@author: Krish
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        processed = {}
        for i in xrange(len(num)):
            if target-num[i] in processed:
                return [processed[target-num[i]]+1,i+1]
            processed[num[i]]=i
            

                