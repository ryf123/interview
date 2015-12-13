class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row ==0:
            return False
        col = len(matrix[0])
        start,end = 0,row-1
        while start <end:
            mid = (start+end)/2
            if matrix[mid][0] > target:
                end = mid-1
            elif matrix[mid][0] < target:
                start = mid+1
            else:
                return True
        row = end if target>=matrix[end][0] else end-1
        start,end = 0,col-1
        while start <=end:
            mid = (start+end)/2
            if matrix[row][mid] < target:
                start = mid+1
            elif matrix[row][mid] > target:
                end = mid-1
            else:
                return True
        return False
matrix = [[0,1,2],[3,5,6]]
s = Solution()
assert(s.searchMatrix(matrix,5))
assert(s.searchMatrix(matrix,7) == False)
assert(s.searchMatrix(matrix,4) == False)
matrix= [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
assert(s.searchMatrix(matrix,11) == True)
matrix = [[-10,-8],[-6,-5],[-2,-2],[-1,0],[3,4],[7,7],[8,9],[10,10],[11,11],[12,14],[15,16],[17,19],[20,21],[22,22],[25,27],[28,30],[32,32],[35,36]]
assert(s.searchMatrix(matrix,16) == True)