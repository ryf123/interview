from collections import defaultdict
class Solution:
	# @param {int} n an integer
	# @param {int[][]} edges a list of undirected edges
	# @return {boolean} true if it's a valid tree, or false
	def validTree(self, n, edges):
		if len(edges) == 0:
			return True if n==1 else False
		# Write your code here
		d = defaultdict(list)
		for edge in edges:
			d[edge[0]].append(edge[1])
			d[edge[1]].append(edge[0])
		self.visited = {}
		self.processed = {}
		for node in d:
			if not self.dfs(d,node,None):
				return False
		return n == len(self.processed)
	def dfs(self,d,node,prev):
		if node in self.visited and self.visited[node]:
			return False
		if node in self.processed and self.processed[node]:
			return True
		self.processed[node] = True
		self.visited[node] = True
		if node in d:
			for child in d[node]:
				if prev!= None and child == prev:
					continue
				if not self.dfs(d,child,node):
					return False
		self.visited[node] = False
		return True
s = Solution()
n,edges = 5,[[0, 1], [0, 2], [0, 3], [1, 4]]
assert(s.validTree(n,edges))
n,edges = 5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
assert(s.validTree(n,edges) == False)

