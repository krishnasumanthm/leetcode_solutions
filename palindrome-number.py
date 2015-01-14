class Solution:
    # @return a boolean
    def reverse_temp(self,x):
        num = 0
        while(x>0):
            r = x%10
            num = num*10+r
            x= x/10
        return num

    def isPalindrome(self, x):
        if x<0:
            return False
        if x == self.reverse_temp(x):
            if math.fabs(x) > math.pow(2,31)-1:
                return False
            else:
                return True
        else:
            return False