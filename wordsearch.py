# trie tree to store words
class TreeNode:
	def __init__(self,val):
		self.val = val
		self.child = {}
		self.end = False
	# add tree node child to it
	def add_child(self,tn):
		self.child[tn.val] = tn
class TrieTree():
	def __init__(self,words):
		self.head = self.buildTree(words)

	# return True if word is found else False
	# input word,start node default is head
	# 
	def getword(self,word,start):
		l = len(word)
		pos = 0 
		stack = [[start,pos]]
		# starts from word position 0
		while(stack):
			[node,pos] = stack.pop()
			if pos == l:
				if node.child:
					return False
				else:
					return True
			c = word[pos]
			if c in node.child:
				stack.append([node.child[c],pos+1])
		return False
	def buildTree(self,words):
		head = TreeNode("")
		for word in words:
			wl  = len(word)
			current = head
			for i,w in enumerate(word):
				if w in current.child:
					current = current.child[w]
				else:
					node = TreeNode(w)
					current.add_child(node)
					current = node
				if i == wl-1:
					current.end = True 
		return head
class Solution:
	# :type board: List[List[str]]
	# @param {string} word
	# @return {boolean}
	def findWords(self, board, words):
		self.board = board
		ret = False
		m = len(board) #row
		if m == 0:
			return []
		n = len(board[0]) #coloumn
		tt = TrieTree(words)
		self.tt = tt
		self.ret = []
		self.visit = [[False]*n  for x in xrange(m)]
		for i in range(0,m):
			for j in range(0,n):
				self.matchword(self.visit,tt.head,i,j,m,n,[])
		return list(set(self.ret))

	def matchword(self,visit,current,i,j,m,n,matched):
		# print i,j
		if self.visit[i][j]:
			return False
		self.visit[i][j] = True
		c = self.board[i][j]
		if c in current.child:
			current = current.child[c]
		else:
			self.visit[i][j] =  False
			return
		matched.append(current.val) 
		if current.end :
			self.ret.append("".join(matched))
			# return 
		
		if j+1 < n:
			if self.matchword(self.visit,current,i,j+1,m,n,matched):
				return 
		if i+1<m:
			if self.matchword(self.visit,current,i+1,j,m,n,matched):
				return 
		if i-1>=0:
			if self.matchword(self.visit,current,i-1,j,m,n,matched):
				return 
		if j-1>=0:
			if self.matchword(self.visit,current,i,j-1,m,n,matched):
				return 
		matched.pop()
		self.visit[i][j]= False
		return False


s = Solution()
board = ["ab","cd"]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
print s.findWords(board,words)