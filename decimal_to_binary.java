String decimal_to_binary(int num){
	boolean sign = false;
	if(num < 0){
		sign = true;
		num = -num;
	}
	int[] nums = new int[32];
	int i = 31;
	while(num > 0){
		nums[i--] = num % 2;
		num /= 2; 
	}
	if(sign){
		reverse(); // 2's complement, reverse then plus 1
		increment();
	}
	StringBuilder sb  = new StringBuilder();
	for(int i=0;i<nums.length;i++){
		sb.add(nums[i]);
	}
	return sb.toString();
}
private void reverse(int[] nums){
	for(int i=0;i<nums.length;i++){
		nums[i] = nums[i] ^ 1;
	}
}
// add 1 to the array
private void increment(int[] nums){
	for(int i=nums.length-1;i>=0;i--){
		if(nums[i] == 1){
			nums[i] = 0;
		}
		else{
			nums[i] = 1;
			break;
		}
	}
}