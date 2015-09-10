class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		s= s.lstrip()
		s = s.rstrip()
		num = False
		dot = False
		exp = False
		sign = False
		s = s.lstrip("+")
		s = s.lstrip("-")
		for i,c in enumerate(s):
			if c.isdigit():
				num  = True
			elif c==".":
				if exp or dot:
					return False
				dot = True
			elif c=="e":
				if exp or not num:
					return False
				num = False
				exp = True
			elif c=="+" or c=="-":
				if i==0:
					return False
				if s[i-1] != "e":
					return False
			else:
				return False
		return num
tests = ["0","2e10","1 a"," 0.1 ","01","0.1e123","123e+123","1e0.1","e9",". 1","-1."]
s = Solution()
for t in tests:
	print t,s.isNumber(t)