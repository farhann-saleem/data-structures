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
    
    def _resize(self):  # helper function - Abstraction
        new_storage= [None] * (self.capacity *2 )    
        for i in range(self.size):
            new_storage[i]=self.storage[i]
            
        self.storage=new_storage
        # this lines doesnt copy it  . it changes teh refrence- so old one doesnt point to anything - garbage cleared
        self.capacity *= 2
        
        
    def get(self,index):
        if 0 <= index < self.size :
            return self.storage[index]
        raise IndexError("index out of range")
        
        
    def set(self ,  index , value ):
        if 0 <=index <self.size:
            self.storage[index]=value 
            return  
        raise IndexError("Index out of range")
    
    def insert(self , index , value):
        #validate inputs first 
        if not (0 <=index <= self.size):
            raise IndexError("Index out of range-No Insertion")
        
        #resize if needed 
        if self.size == self.capacity :
            self._resize()
        
        #main operation    
        for i in range(self.size -1 , index -1 , -1):
            self.storage[i +1]= self.storage[i] 
        
        #update 
        self.storage[index]=value
        self.size +=1
            
    def remove(self , index):
        if not (0 <=index < self.size):
            raise IndexError("Index out of range - cant remove")

        for i in range( index , self.size -1 ):
            self.storage[i] = self.storage[i+1]
            
        self.storage[self.size -1 ]=None
        self.size -=1
            
    def __len__(self):
        return self.size
            
    def __str__(self):
        result = "["
        for i in range(self.size):
            result +=  str(self.storage[i])
            if i != self.size -1:
                result += ", "
        result += "]"
        return result
arr=Dynamic_Array()
arr.append(20)
arr.append(30)
arr.append(40)
# arr.set(80,1)


print(arr.storage)
print(arr.get(1))
arr.set(2 , 80)
arr.insert(3,75)
arr.append(40)
arr.remove(0)

print(arr.__len__())
print(arr)
print(arr.storage)
