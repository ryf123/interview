class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0]) if self.row else 0
        dp = [[0]*(self.col+1) for x in xrange(self.row+1)]
        # for row in range(0,self.row):
        #     dp[row][0] = (dp[row-1][0] if row>0 else 0) + matrix[row][0]
        # for col in range(0,self.col):
        #     dp[0][col] = (dp[0][col-1] if col>0 else 0) + matrix[0][col]  
        for row in range(0,self.row):
            for col in range(0,self.col):
                dp[row+1][col+1] = dp[row][col+1] + dp[row+1][col] + matrix[row][col] - dp[row][col]
        self.dp = dp
        print dp
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row2 >= self.row or col2>=self.col or row1<0 or col1<0:
            return 0
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

matrix = [[1,2],[2,1]]
n = NumMatrix(matrix)
print n.sumRegion(0,0,1,1)

