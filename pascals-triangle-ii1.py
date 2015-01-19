class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        out = [1]
        if rowIndex == 0:
            return out
        elif rowIndex == 1:
            out.append(1)
        else:
            out.append(1)
            for i in xrange(2,rowIndex+1,1):
                for j in xrange(i-1):
                    out[j] = out[j]+out[j+1]
                out.insert(0,1)
        return out