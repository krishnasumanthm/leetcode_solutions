class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.data = []
        self.minval = []
    
    # @return nothing    
    def push(self, x):
        self.data.append(x)
        if len(self.minval) == 0 or x<=self.minval[-1]:
            self.minval.append(x)
    
    # @return an integer
    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            if self.data[-1] == self.minval[-1]:   
                self.minval.pop()
            return self.data.pop()
 
    # @return an integer
    def top(self):
        if len(self.data) == 0: 
            return None
        else:
            return self.data[-1]
 
    # @return an integer
    def getMin(self):
        if len(self.minval) == 0:  
            return None
        else:          
            return self.minval[-1]