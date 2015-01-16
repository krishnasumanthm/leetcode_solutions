class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits[-1] += 1
        carry = 0
        for index in xrange(len(digits)-1, -1, -1):
            digits[index] += carry
            carry = digits[index] // 10
            if carry == 0:      
                break
            else:               
                digits[index] %= 10
        else:
            
            digits.insert(0, 1)
        
        return digits