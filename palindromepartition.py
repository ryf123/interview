class Solution:
	# @param {string} s
	# @return {string[][]}
	def partition(self, s):
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
					for t in partitionsubstring(i+1,end):
					    ret.append([s[start:i+1]]+t)
			return ret
		l = len(s)
		return partitionsubstring(0,l-1)
s = Solution()
st = "aab"
print s.partition(st)