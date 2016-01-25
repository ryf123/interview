class Solution(object):
	def ladderLength(self, beginWord, endWord, wordDict):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordDict: Set[str]
		:rtype: int
		"""

		wordDict = list(wordDict)
		if len(wordDict) == 0:
			return False
		d = {}
		begin_set = {beginWord:True}
		end_set = {endWord:True}
		for word in wordDict:
			d[word] = True
		level = 0
		while len(begin_set) and len(end_set):
			level +=1
			if len(begin_set) <= len(end_set):
				set1,set2 = begin_set,end_set
				flag = True
			else:
				set1,set2 = end_set,begin_set
				flag = False
			inter_set  = {}
			for word in set1:
				l  = len(word)
				for x in xrange(l):
					for c in xrange(26):
						c = chr(97+c)
						word2 = word[:x]+c+word[x+1:]
						if word2 in set2:
							return level +1
						if word2 in d:
							del d[word2]
							inter_set[word2] = True
				if flag:
					begin_set = inter_set
				else:
					end_set = inter_set
		return 0
s = Solution()
print s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])