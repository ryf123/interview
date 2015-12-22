#include "iostream"
#include "unordered_set"
#include "vector"
using namespace std;
class Solution {
public:
	std::vector<string> ret;
	vector<vector <string> > dp;
	 // vector<vector <string> > prime();
    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
    	dp.resize(s.size()+1);
    	if(s.size() == 0){
    		return ret;
    	}
 		dp[0].push_back("");
		for(int i=0;i<=s.size();++i){
			if (dp[i].size()>0)
			 {
			 	for (string word:wordDict)
			 	{
			 		if(i+word.size() <= s.size()){
			 			// cout<<word<<endl;
			 			// cout<<s.substr(i,word.size())<<endl;
				 		if(word == s.substr(i,word.size())){
				 			
				 			dp[i+word.size()].push_back(word);	
				 		}
			 		}

			 	}
			 }
		}
		// cout<<s<<endl;
		vector<string> path;
		dfs(s,s.size(),path);
	 	return ret;   
    }
    void dfs(string s,int end,vector<string> path){
    	// cout<<end<<endl;
    	if (end < 0){
    		return;
    	}
    	if (end== 0 )
    	{
    		// cout<<end<<endl;
    		string string_path = "";
    		for(string word:path){
    			// cout<<word<<endl;
    			string_path = word + " " + string_path;
    		}
    		ret.push_back(string_path.substr(0,string_path.size()-1));
    		return;
    	}
    	if (dp[end].size() > 0)
    	{
    		for (int i = 0; i < dp[end].size(); ++i)
    		{
    			path.push_back(dp[end][i]);
    			dfs(s,end-dp[end][i].size(),path);
    			path.pop_back();
    		}
    	}
    	
    }
};
int main(int argc, char const *argv[])
{
	Solution sl;
	string s = "catsanddog";
	// unordered_set<string> third ( {"orange","pink","yellow"} );
	// std::unordered_set<std::string> second ( {"red","green","blue"} );
	unordered_set<string> wordDict( {"cat", "cats", "and", "sand", "dog"} );
	for(string st:sl.wordBreak(s,wordDict)){
		cout<<st<<endl;
	}
	return 0;
}