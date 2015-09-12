class Solution(object):

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""
		l = len(s)
		mark = [] *l
		mark = [[] for x in xrange(l+1)]
		mark[0].append(None)
		# print mark
		i = 1
		for i in range(1,l+1):
			# print i
			if not mark[i-1]:
				# print i
				continue
			for word in wordDict:

				wl = len(word)
				# print s[i-1:i+wl-1],word
				if s[i-1:i+wl-1] == word:
					mark[i+wl-1].append(word)
		# print mark
		self.ret = []
		self.dfs(l,mark,[])
		return self.ret
	def dfs(self,end,mark,path):
		# print path,[end]
		if end == 0:
			self.ret.append(" ".join(path))
			return
		if mark[end]:
			words = mark[end]
			for word in words:
				self.dfs(end-len(word),mark,[word]+path)
sl = Solution()
s,d = "catsanddog",["cat", "cats", "and", "sand", "dog"]
print sl.wordBreak(s,d)

