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
					temp = partitionsubstring(i+1,end)
					if len(temp) > 0:
						for t in temp:
							ret.append([s[start:i+1]]+t)
			return ret

		partarray = []
		l = len(s)

		for i in range(0,l-1):
			if ispanlindorme(s[0:i+1]):
				ps = partitionsubstring(i+1,l-1)
				if len(ps) > 0:
					for p in ps:
						temp =[s[0:i+1]] + p
						partarray.append(temp)
		if ispanlindorme(s):
			print s
			partarray.append([s])
		return partarray
s = Solution()
st = "abcdefghlmnoaba"
print s.partition(st)