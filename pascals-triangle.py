class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        out = []
        if numRows == 0:
            return []
        
        for i in xrange(0,numRows,1):
            if i == 0:
                out.append([1])
            else:    
                temp = []
                for j in xrange(i+1):
                    if j == 0 or j == i:
                        temp.append(1)
                    else:
                        temp.append(out[i-1][j-1]+out[i-1][j])
                out.append(temp)
        return out