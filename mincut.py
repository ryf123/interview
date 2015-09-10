class Solution(object):
	def minCut(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		def ispanlindorme(p):
			return True if p == p[::-1] else False
		def partitionsubstring(start,end):
			ret = []
			if ispanlindorme(s[start:end+1]):
				ret.append([s[start:end+1]])
			if start == end:
				return ret
			for i in range(start,end):

				if ispanlindorme(s[start:i+1]):
					temp = partitionsubstring(i+1,end)
					if len(temp) > 0:
						for t in temp:
							ret.append([s[start:i+1]]+t)
			return ret
		if ispanlindorme(s):
			return 0
		partarray = []
		l = len(s)
		min = l
		for i in range(0,l-1):
			if ispanlindorme(s[0:i+1]):
				ps = partitionsubstring(i+1,l-1)
				if len(ps) > 0:
					for p in ps:
						temp =[s[0:i+1]] + p
						partarray.append(temp)
						if len(temp) < min:
							min = len(temp) - 1
		return min
s = Solution()
print s.minCut("a")