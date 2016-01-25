class Solution(object):
	def isAdditiveNumber(self, num):
		"""
		:type num: str
		:rtype: bool
		"""
		l = len(num)
		for i in xrange(l):
			for j in range(i+1,l):
				num1,num2 = num[:i+1],num[i+1:j+1]
				if self.dfs(num,num1,num2,j+1):
					return True
		return False
	def dfs(self,num,num1,num2,start):
		if (num1[0] == "0" and num1 != "0") or (num2[0] == "0" and num2 != "0"):
			return False
		s = self.add(num1,num2)
		for i in range(start,len(num)):
			if num[start:i+1] == s:
				if i+1 == len(num):
					return True
				return self.dfs(num,num2,s,i+1)
		return False
	def add(self,num1,num2):
		count = 0
		addon = 0
		ret = ""
		while count<len(num1) or count<len(num2):
			a = num1[0-count-1] if count < len(num1) else 0
			b = num2[0-count-1] if count< len(num2) else 0
			s =  int(a)+int(b)+addon
			addon = s/10
			ret = str(s%10) +ret
			count +=1
		return "1"+ret if addon else ret
s = Solution()
print s.isAdditiveNumber("101")
