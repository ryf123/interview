class Solution(object):
	def candy(self, ratings):
		"""
		:type ratings: List[int]
		:rtype: int
		"""
		l,i = len(ratings),1
		if l == 0:
			return 0
		candies = [1] * l
		while i <l:
			if candies[i] <= candies[i-1] and ratings[i] > ratings[i-1]:
				candies[i] = candies[i-1]+1
			i+=1
		i = l-2
		while i>=0:
			if candies[i] <= candies[i+1] and ratings[i] > ratings[i+1]:
				candies[i] = candies[i+1]+1
			i-=1
		# print candies
		return sum(candies)
s = Solution()
ratings = [1,4,5,2,3,1]
ratings = [1,2,2,1]
print s.candy(ratings)
