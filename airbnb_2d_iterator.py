# Given an array of arrays, implement an iterator class to allow the client to traverse and remove elements in the array list.  This iterator should provide three public class member functions:
# boolean hasNext()
#   return true or false if there is another element in the set
# int next()
#   return the value of the next element in the array (if array stores int)
# void remove()
#   remove the last element returned by the iterator.  That is, remove the element that the previous next() returned
#   This method can be called only once per call to next(), otherwise, an exception will be thrown. 
#

class Array_Iterator:
    def __init__(self,array):
        self.array = array
        self.row = len(array)
        self.row_p = 0
        self.col_p = -1
    def next(self):
        if self.row_p < self.row:
            current_col = len(self.array[self.row_p])
            if self.col_p + 1 < current_col:
                self.col_p +=1
                return self.array[self.row_p][self.col_p]
            else:
                self.row_p +=1
                while self.row_p<self.row and len(self.array[self.row_p]) == 0:
                    self.row_p+=1
                if self.row_p < self.row:
                    self.col_p = 0
                    return self.array[self.row_p][self.col_p]
    def hasNext(self):
        row_p,col_p = self.row_p,self.col_p
        if row_p < self.row:
            if col_p +1 < len(self.array[row_p]):
                return True
            else:
                row_p+=1
                while row_p < self.row and len(self.array[row_p]) == 0:
                    row_p +=1
                if row_p < self.row:
                    return True
        return False
    
    def remove(self):
        if self.row_p < self.row and self.col_p != -1:
            self.array[self.row_p].pop(self.col_p)
            self.col_p -=1
array = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]

# Remove even elements (with even indices)
ai = Array_Iterator(array)
count = 0
row = len(array)

while ai.hasNext():
    print ai.next()
    ai.remove()
print ai.array

                
    
    