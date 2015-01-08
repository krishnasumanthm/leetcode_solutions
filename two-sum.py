# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        temp = {}
        for i in xrange(len(num)):
            if target-num[i] in temp:
                index1 = temp[target-num[i]]+1
                index2 = i+1
                return index1,index2
            temp[num[i]]=i
            

                