class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0 
        # indiacated index where item is to be insterted 
        self.buffer = [None]*capacity
        # creates an array  with length equal to the provided capacity 

    def append(self, item):
        self.buffer[self.index] = item
        # puts item at currently staged index withon buffer
        self.index += 1
        # changes the curenlty staged index to the next index 
        if self.index == self.capacity:
        	self.index = 0 
        	#  if last index is reached , insdex geets reset to 0 


    def get(self):
        results = []
        for i in self.buffer:
            if i != None:
                results.append(i)

        return results