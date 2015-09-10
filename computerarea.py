class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""
		area1 = (C-A)*(D-B)
		area2 = (G-E)*(H-F)
		if E> C or G < A or F> D or H <B:
			return area1+area2
		else:
			# print area1,area2
			xaxis = [E,A,G,C]
			yaxis = [H,D,F,B]
			xaxis.sort()
			yaxis.sort()
			inter = (xaxis[2]-xaxis[1])*(yaxis[2]-yaxis[1])
			# print inter
			return area1+area2 -inter
s = Solution()
print s.computeArea(0, 0, 2, 2, -1, -1, 1, 1)