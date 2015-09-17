class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		ret = []
		nopre = []
		d = {}
		for x in xrange(numCourses):
			d[x] = {}
		for prerequisite in prerequisites:
			d[prerequisite[0]][prerequisite[1]] = True
		for key in d:
			if len(d[key]) == 0:
				nopre.append(key)
		while len(nopre):
			course = nopre.pop()
			del d[course]
			ret.append(course)
			for key in d:
				if course in d[key]:
					del d[key][course]
					if len(d[key]) == 0:
						nopre.append(key)
		# print ret
		return ret if len(ret) == numCourses else []


s = Solution()
numCourses = 3
prerequisites = [[1,0],[0,2],[1,2]]
print s.findOrder(numCourses,prerequisites)