import math
def solution(nums):
	total = 0
	ceil = [] # saves the pair [ceil(num)-num,index]
	total_floor = 0
	for index,num in enumerate(nums):
		ceil_diff = math.ceil(num)-num
		if ceil_diff >0:
			ceil.append([ceil_diff,index])
		total += num
		nums[index] = math.floor(num)
		total_floor += nums[index]
	round_nums = round(total) # the round number
	# sort the ceil differences by it's difference
	ceil = sorted(ceil,key=lambda x:x[0])
	# difference between total round and sum of each floor
	# if it's greater than 0, then make the num to be ceiling instead of floor
	diff  = round_nums - total_floor
	while diff >0 and len(ceil):
		pair = ceil.pop(0) # pop out the smallest one each time
		nums[pair[1]] += 1
		diff-=1
	print nums
solution([1.2,2.3,3.4])
solution([1.2,1.9,1.8])
solution([1.2,1.3,1.1])
solution([1.2 ,1.2,1.2])
solution([1.6 ,1.6 ,1.6])


