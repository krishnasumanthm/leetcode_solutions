class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        out = [1]
        if rowIndex == 0:
            return out
        if rowIndex == 1:
            return [1,1]
        d = 1
        m = rowIndex
        for i in xrange(rowIndex // 2):
            nextval = (out[-1]*m)/d
            out.append(nextval)
            d += 1
            m -= 1
        if rowIndex % 2 == 1:
            out.extend(out[::-1])
        else:
            out.extend(out[-2::-1])
        return out