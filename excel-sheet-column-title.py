class Solution:
    # @return a string
    def convertToTitle(self, num):
        out = []
        while num > 0:
            print num
            temp = num % 26
            num = num // 26
            if temp == 0:
                out.append('Z')
                num = num-1
            else:
                out.append(chr(65+temp+-1))
        return ''.join(out[::-1]) 