class Solution:
    # @return an integer
    def reverse(self, x):
        if str(x)[0] == '-':
            temp = -1 * int(str(-x)[::-1])
        else:
            temp = int(str(x)[::-1])
        if math.fabs(temp) > math.pow(2,31)-1:
            temp = 0
        return temp