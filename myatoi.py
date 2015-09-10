class Solution(object):
	def myAtoi(self, st):
		"""
		:type str: str
		:rtype: int
		"""
		total = 0
		st = st.lstrip()
		st = st.rstrip()
		if len(st) == 0:
			return 0
		if st[0] == "-":
			neg = True
			st = st[1:]
		else:
			neg = False
			if st[0] == "+":
				st = st[1:]
		# print st
		while st[0] == "0":
			st = st[1:]
		l = len(st)
		# print st
		for i,s in enumerate(st):
			if s.isdigit():
				
				if i>0:
					total*=10
				total += int(s)
				if total >= 2147483647 :
					if not neg:
						return 2147483647
					else:
						if total > 2147483647:
							return -2147483648

			else:
				break
		return total if not neg else -total
s = Solution()
tests = ["10","-10"," ","  -1","111","1","2147483649","-2147483649","  -0012a42","   +0 123"]
for t in tests:
	print s.myAtoi(t)        