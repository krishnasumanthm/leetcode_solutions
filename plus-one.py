class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits[-1] = digits[-1] + 1
        carry = 0
        for i in xrange(len(digits)-1,-1,-1):
            digits[i] = digits[i]+carry
            carry = digits[i]//10
            if carry == 0:
                break
            else:
                digits[i] = digits[i]%10
        else:
            digits.insert(0,1)
        
        return digits