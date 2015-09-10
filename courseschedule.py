class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		def dfs(node):
			# print self.visited
			if self.visited[node] == 1:
				return True
			if self.visited[node] == -1:
				return False
			self.visited[node] = -1
			if node in d:
				for edge in d[node]:
					if not dfs(edge):
						return False
			self.visited[node] = 1
			self.ret.append(node)
			return True
		self.visited = [0] * numCourses
		d = {}
		self.ret = []
		for p in prerequisites:
			if p[0] in d:
				d[p[0]].append(p[1])
			else:
				d[p[0]] = [p[1]]
		# print d
		for node in xrange(numCourses):
			if not dfs(node):
				return []
		return self.ret
s = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print s.findOrder(numCourses,prerequisites)