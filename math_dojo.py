class MathDojo:
    
    def __init__(self):
        self.result = 0
    
    def __repr__(self):
        return str(self.result)
    
    def addition(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
    
    def subtraction(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self

# create an instance:
md = MathDojo()

# to test:
md.addition(2,5,1,6,78).subtraction(5,2,23)
print(repr(md))	# Should print 62


