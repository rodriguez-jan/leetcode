class MaxStack(object):

    #Want to store boh th element and its respective max in a tuple for every item pushed in
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        mx = max(x,self.stk[-1][1] if self.stk else None)
        self.stk.append((x,mx))
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stk.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1][0]
        
        

    def peekMax(self):
        """
        :rtype: int
        """
        
        return self.stk[-1][1]
        

    def popMax(self):
        """
        :rtype: int
        """
        #find max element
        #pop items off the stack that are not the max element
        #push them back on when done
        find = self.stk[-1][1]
        tempArr = []
        while(find != self.top()):
            tempArr.append(self.pop())
        tempMax = self.pop()
        map(self.push,reversed(tempArr))
        
        return tempMax
        
        
        
        
