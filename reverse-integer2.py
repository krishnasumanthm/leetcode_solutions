class Solution:
    # @return an integer
    def reverse_temp(self,x):
        num = 0
        while(x>0):
            r = x%10
            num = num*10+r
            x= x/10
        return num
    def reverse(self, x):
        if x<0:
            temp = self.reverse_temp(x*(-1))*(-1)
        else:
            temp = self.reverse_temp(x)
        if math.fabs(temp) > math.pow(2,31)-1:
            temp = 0
        return temp