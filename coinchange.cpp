#include <iostream>
#include "vector"
#include "list"
using namespace std;
class Solution {
public:
	int total;
    int coinChange(vector<int>& coins, int amount) {
    	vector<int> dp = {amount+1,INT_MAX};
    	dp[0] = 0;
    	int j = 1;
    	while(j<=amount){
    		for (int i = 0; i < coins.size(); ++i)
    		{
    			if(j-coins[i]>=0 && dp[j-coins[i]] != INT_MAX){
    				dp[j] = min(dp[j],dp[j-coins[i]]+1);
    			}
    		}
    		j++;
    	}
    	return dp[amount]==INT_MAX?-1:dp[amount];
    }
};