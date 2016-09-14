package test;
import java.util.*;
public class SubarrayProduct {
	boolean product_sum(int[] nums,int target){
		Set<Long> set = new HashSet();
		set.add(new Long(1));
		long product = 1;
		if(target == 0){
			for(int num:nums)
				if(num == 0)
					return true;
			return false;
		}
		for(int i=0;i<nums.length;i++){
			if(nums[i] == 0){
				set.clear();
				set.add(new Long(1));
				product = 1; // initialize, we don't care about 0
			}
			else{
				product *= nums[i];
				if(product%target == 0 && set.contains(product/target))
					return true;
				set.add(product);
			}
		}
		return false;
	}
	public static void main(String args[]){
		SubarrayProduct sp = new SubarrayProduct();
		int[] nums = {2,3,4,5,0,-10,-20};
		int target = 120;
		System.out.println(sp.product_sum(nums, target));
		target = 12;
		System.out.println(sp.product_sum(nums, target));
		target = 200;
		System.out.println(sp.product_sum(nums, target));
		
	}
}
