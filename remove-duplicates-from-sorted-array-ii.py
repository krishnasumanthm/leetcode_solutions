class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates_temp(self, A, m):
        if not A:
            return len(A)
        else:
            count = 1
            temp = 0
            prev = A[0]
            for i in xrange(1,len(A)):
                if A[i]!=prev:
                    A[temp+1] = A[i]
                    temp = temp+1
                    prev = A[i]
                    count = 1
                else:
                    if count<m:
                        A[temp+1] = A[i]
                        temp = temp+1
                        prev = A[i]
                        count = count +1
        A = A[0:temp+1] 
        return len(A)
    
    def removeDuplicates(self, A):
        return self.removeDuplicates_temp(A, 2)
            