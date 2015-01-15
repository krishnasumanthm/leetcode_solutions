class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX, INT_MIN = 2147483647, -2147483648
        index = 0
        result = 0
        sign = 1        
        if len(str) == 0:   return 0
 
        while str[index].isspace():     
            index += 1  
 
        if str[index] == "-":           
            sign = -1
        if str[index] in "-+":          
            index += 1  
 
        while index < len(str) and str[index].isdigit():
            result = result * 10 + (ord(str[index]) - ord("0")) * sign
            index += 1
            if sign == 1 and result >= INT_MAX:     
                return INT_MAX
            elif sign == -1 and result <= INT_MIN:  
                return INT_MIN
 
        return result