class WordNode:
	def __init__(self,val):
		self.val = val
		self.prev = None
class Solution(object):
	def getret(self,wn,s):
		ret = []
		if wn.prev != None:
			for w in wn.prev:
				return ret.append(self.getret(w,wn.val+s))
		else:
			r = wn.val+s
			return r[::-1]
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""
		l = len(s)
		mark = [] *l
		mark = [[] for x in xrange(l)]
		mark[0].append(None)
		for i,w in enumerate(s):
			print i
			if not mark[i]:
				continue
			for word in wordDict:
				wl = len(word)
				# print s[i+1:i+wl],word,i+wl-1
				if s[i+1:i+wl+1] == word:
					# print word,word
					wn = WordNode(word)
					wn.prev = mark[i]
					mark[i+wl-1].append(wn)
					print i,i+wl-1,wn.val,word
					# print len(mark[i])
		ret = []
		# print mark
		# for m in mark:
		# 	for x in m:
				# if x:
					# print x
					# print x.val
			# print "+++++" 
		# print mark
		# if len(mark[l-1]) > 0:
		# 	for wn in mark[l-1]:
		# 		ret.append(self.getret(wn,""))
		# return ret
sl = Solution()
s,d = "catsanddog",["cat", "cats", "and", "sand", "dog"]
print sl.wordBreak(s,d)

