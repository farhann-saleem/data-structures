class Dynamic_array:
    
    def __init__(self):
        self.capacity=2
        self.size=0
        self.storage=[None] * self.capacity
        
    def ammend(self , value):
        if self.capacity == self.size :
            self._resize()
        
        self.storage[self.size]=value
        self.size +=1 
        
        
    def _resize(self):
        
        new_storage= [None] * (self.capacity*2)
        
        for i in range(self.size):
            new_storage[i]=self.storage[i]
            
        self.storage=new_storage
        self.capacity *=2
        
arr=Dynamic_array()
arr.ammend(10)
arr.ammend(30)
arr.ammend(40)
arr.ammend(80)
arr.ammend(40)
arr.ammend(80)

print(arr.capacity)
print(arr.size)
print(arr.storage)
