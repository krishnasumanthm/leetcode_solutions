class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for val in A:
            twos  = twos | (ones & val)
            ones  = ones ^ val
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones