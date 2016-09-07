import java.util.Arrays;

public class palindromesubset {


	  public int maxsubset(int[] nums){
	    if(nums==null || nums.length == 0) return 0;
	    int n = nums.length;
	    int[][] dp = new int[n][n];
	    int maxlength = 1;
	    for(int i=0; i<n; i++){
	      dp[i][i] = 1; // each number is a palindrome with length 1
	    }
	    for(int i=0; i<n-1; i++){
	        if(nums[i] == nums[i+1]){
	            dp[i][i+1] = 2; // the adj numbers are the same, then they can form a palindrome with length 2
	            maxlength = 2;
	        }
	        else
	            dp[i][i+1] = 1;
	    }
	    int i = 2;
	    while(i<n){
	      for(int j=0; j<n-i; j++){
	          if(nums[j] == nums[j+i]){
	              dp[j][j+i] = dp[j+1][j+i-1] + 2; // if tail head number are equal, add 2 e.g [2,0,0,2]
	              maxlength = Math.max(maxlength,dp[j][j+i]);
	          }
	          else{
	              dp[j][j+i] = Math.max(dp[j+1][j+i],dp[j][j+i-1]);
	          }
	      }
	      i++;
	    }
	    return maxlength;
	  }
	 
	  public static void main(String[] args) {
	    int[] nums1 = {1,2,2,0,1};
	    int[] nums2 = {0,2,2,3,3,4,5,6,2};
	    palindromesubset solution = new palindromesubset();
	    System.out.println(solution.maxsubset(nums1));
	    System.out.println(solution.maxsubset(nums2));
	  }
}
