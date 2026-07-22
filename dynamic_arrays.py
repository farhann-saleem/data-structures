class Dynamic_Array:
    def __init__(self):
        self.capacity=2
        self.size=0
        self.storage= [None] * self.capacity
        
    def append(self , value):
        if self.size == self.capacity:
            self._resize()
        
        self.storage[self.size]= value
        self.size +=1 
    
    def _resize(self):
        new_storage= [None] * (self.capacity *2 )    
        for i in range(self.size):
            new_storage[i]=self.storage[i]
            
        self.storage=new_storage
        # this lines doesnt copy it  . it changes teh refrence- so old one doesnt point to anything - garbage cleared
        self.capacity *= 2
        
        
arr=Dynamic_Array()
arr.append(20)
arr.append(30)
arr.append(40)



print(arr.storage)
