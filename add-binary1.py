class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        num1 = 0
        num2 = 0
        for digit in a:
            num1 = 2*num1 + int(digit)
        for digit in b:
            num2 = 2*num2 + int(digit)
        sum = num1+num2
        temp = []
        if sum == 0:
            return '0'
        else:
            while(sum>0):
                temp.append(str(sum%2))
                sum = sum/2
            
        return ''.join(temp)[::-1]