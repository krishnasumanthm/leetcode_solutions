class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        temp = {}
        res = []
        for str in strs:
            temp_str = ''.join(sorted(str))
            if temp_str in temp:
                x = temp[temp_str]
                x.append(str)
                temp[temp_str] = x
            else:
                temp[temp_str] = [str]
        for i in temp.values():
            if len(i)>1:
                res = res + i
        return res