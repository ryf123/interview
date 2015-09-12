class Solution(object):
	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		ret = []
		l = len(words)
		i = 0
		while i<l:
			# print words[i]
			rowlen = 0
			rowstr = []
			j = i
			# print [words[i]]
			while j<l and rowlen + len(words[j]) <=maxWidth:
				rowstr.append(words[j]) 
				rowlen += len(words[j])
				if rowlen+1 < maxWidth:
					rowlen+=1 # add space
				elif rowlen+1 == maxWidth:
					break
				j+=1
			if rowlen == maxWidth:
				ret.append(" ".join(rowstr))
			else:
				if i+ len(rowstr) != l: # if it's not the last line
					# pad space to words
					leftspace = (maxWidth - len("".join(rowstr)))
					if len(rowstr) == 1:
						for x in xrange(leftspace):
							rowstr[0] += " "
						ret.append(rowstr[0])
						i+=1
						continue
					k = 1
					while leftspace >0:
						# print [leftspace,k]
						spacewidth = leftspace/max(1,len(rowstr)-k)
						spacestr = ""
						for x in xrange(spacewidth):
							spacestr += " "
						# print [spacestr]
						for x in xrange(len(rowstr)-k):
							rowstr[x] += spacestr
							leftspace -= len(spacestr)
						k+=1
					ret.append("".join(rowstr))
				else:
					padspace = ""
					leftspace = (maxWidth - len(" ".join(rowstr)))
					for x in xrange(leftspace):
						padspace += " "
					ret.append(" ".join(rowstr)+padspace)

			i+= len(rowstr)
			# print i,rowstr
		return ret
s = Solution()
words,L =  ["This", "is", "an", "example", "of", "text", "justification."],16
# words,L = ["What","must","be","shall","be."], 12
# words,L = ["ours","to","see","Que","sera","sera","When","I","was","just","a","child","in","school","I","asked","my","teacher","what","should","I","try","Should","I","paint","pictures"], 60
for st in s.fullJustify(words,L):
	print len(st),st