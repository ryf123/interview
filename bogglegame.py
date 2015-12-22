from collections import Counter
class Boggle():
	def search(self,matrix,word):
		worddict = Counter()
		for c in word:
			worddict[c] +=1
		row = len(matrix)
		if row ==0:
			return False
		col = len(matrix[0])
		if col == 0:
			return False
		self.visited = [[False] * col  for x in xrange(row)]
		for i in xrange(row):
			for j in xrange(col):
				if matrix[i][j] in worddict:
					matcheddict = Counter()
					matcheddict[matrix[i][j]] +=1
					if self.dfs(matrix,word,matrix[i][j],worddict,matcheddict,i,j,row,col):
						return True
		return False
	def dfs(self,matrix,word,matched,worddict,matcheddict,i,j,row,col):
		if self.visited[i][j]:
			return False
		self.visited[i][j] = True
		mathced_l = len(matched)
		if  mathced_l == len(word):
			if sorted(matched) == sorted(word):
				return True
			else:
				self.visited[i][j] = False
				return False
		if i-1>=0:
			next = matrix[i-1][j]
			next_i = i-1
			next_j = j
			if next in worddict:
				if matcheddict[next] +1 <= worddict[next]:
					matcheddict[next] +=1
					if self.dfs(matrix,word,matched+next,worddict,matcheddict,next_i,next_j,row,col):
						return True
						next = matrix[i-1][j]
		if i+1 <row:
			next = matrix[i+1][j]
			next_i = i+1
			next_j = j
			if next in worddict:
				if matcheddict[next] +1 <= worddict[next]:
					matcheddict[next] +=1
					if self.dfs(matrix,word,matched+next,worddict,matcheddict,next_i,next_j,row,col):
						return True

						next = matrix[i-1][j]
		if j-1>=0:
			next = matrix[i][j-1]
			next_i = i
			next_j = j-1
			if next in worddict:
				if matcheddict[next] +1 <= worddict[next]:
					matcheddict[next] +=1
					if self.dfs(matrix,word,matched+next,worddict,matcheddict,next_i,next_j,row,col):
						return True
						next = matrix[i-1][j]
		if j+1 < col:
			next = matrix[i][j+1]
			next_i = i
			next_j = j+1
			if next in worddict:
				if matcheddict[next] +1 <= worddict[next]:
					matcheddict[next] +=1
					if self.dfs(matrix,word,matched+next,worddict,matcheddict,next_i,next_j,row,col):
						return True
		self.visited[i][j] = False
		return False
st = "ECEA,ALEP,HNBO,QTTY"
st = st.split(",")
matrix = [row[:] for row in st]
b = Boggle()
assert(b.search(matrix,"PEACE"))
assert(b.search(matrix,"CELEB"))
assert(b.search(matrix,"ELAN"))
assert(b.search(matrix,"CAPE"))
assert(not b.search(matrix,"POPE"))


