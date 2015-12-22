from collections import defaultdict
class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		self.d = defaultdict(list)
		for prerequisite in prerequisites:
			self.d[prerequisite[0]].append(prerequisite[1])
		self.processed = []
		self.visited = {}
		for course in xrange(numCourses):
			if not self.dfs(course):
				return []
		if numCourses == len(self.processed):
			return self.processed
		else:
			return []
	def dfs(self,course):
		if course in self.visited and self.visited[course]:
			return False
		if course in self.processed:
			return True
		self.visited[course] = True
		if course in self.d:
			for prerequisite in self.d[course]:
				if not self.dfs(prerequisite):
					return False
		self.visited[course] = False
		self.processed.append(course)
		return True




s = Solution()
numCourses = 3
prerequisites = [[1,0],[0,2],[1,2]]
numCourses = 1
prerequisites = []
numCourses = 2
prerequisites = [[0,1]]
print s.findOrder(numCourses,prerequisites)