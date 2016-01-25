class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> ret;
        vector<int> path;
        helper(1,ret,path,n,k);
        return ret;
    }
    void helper(int start,vector<vector<int>> &ret,vector<int> path,int n,int k){
    	if (n==0 && k==0){
    		ret.push_back(path);
    	}
    	if(n<=0 || k==0){
    		return;
    	}
    	while(start<=9){
    		path.push_back(start);
    		helper(start+1,ret,path,n-start,k-1);
    		path.pop_back();
    		start++;
    	}
    }
};