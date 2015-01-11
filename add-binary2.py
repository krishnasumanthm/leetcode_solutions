class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        num1 = int(a,2)
        num2 = int(b,2)
        sum = num1+num2
        return bin(sum)[2:] 