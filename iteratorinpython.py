class Counting:
    def __init__(self, limit):
        self.limit = limit
    
    # implementing the __iter__ method
    def __iter__(self):
        self.current = 0
        return self
    
    # implementing the __next__ method
    def __next__(self): 
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
            
if __name__=='__main__':
  # create object of Counting class
  counting = Counting(10)
  
  # use for loop on it
  for x in counting:
    print(x)