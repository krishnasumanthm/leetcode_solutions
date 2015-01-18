class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m_rows = len(matrix)
        if m_rows == 0:
            return []
        m_columns = len(matrix[0])
        out = []
        i = 0
        j = 0
        
        while(i < m_rows and j < m_columns):
            for k in xrange(j,m_columns):
                out.append(matrix[i][k])
            i = i+1
            
            for k in xrange(i,m_rows):
                out.append(matrix[k][m_columns-1])
            m_columns = m_columns-1
            
            if (i < m_rows):
                for k in xrange(m_columns-1,j-1,-1):
                    out.append(matrix[m_rows-1][k])
                m_rows = m_rows-1
            
            if (j < m_columns):
                for k in xrange(m_rows-1,i-1,-1):
                    out.append(matrix[k][j])
                j = j+1
        return out