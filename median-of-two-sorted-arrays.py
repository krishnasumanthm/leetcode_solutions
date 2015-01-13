class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.
    
    #Code for getting kth element in the combined array
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ind_a, ind_b = len(a) // 2 , len(b) // 2
        val_a, val_b = a[ind_a], b[ind_b]
    
        if ind_a + ind_b < k:
            if val_a > val_b:
                return self.kth(a, b[ind_b + 1:], k - ind_b - 1)
            else:
                return self.kth(a[ind_a + 1:], b, k - ind_a - 1)
        else:
            if val_a > val_b:
                return self.kth(a[:ind_a], b, k)
            else:
                return self.kth(a, b[:ind_b], k)