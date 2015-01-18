class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        pattern = re.compile('\W')
        string = re.sub(pattern, '', s.lower())
        if string == string[::-1]:
            return True
        else:
            return False