#include <unordered_map>
#include <string>
#include <sstream>
#include "iostream"
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<string,char> map;
        unordered_map<char,string> pattern_map;
        istringstream ss(str); 
        string token;
        int i = 0; 
        while(std::getline(ss, token, ' ')){
        	if(map.find(token) == map.end()){
        		if(pattern_map.find(pattern[i]) != pattern_map.end())
        			return false;
        		
        		map[token] = pattern[i];
        		pattern_map[pattern[i]] = token;
        	}
        	else if (pattern[i] != map[token])
        	{
        		return false;
        	}
        	i++;

        }
        return i == pattern.size(); 
    }
};
int main(int argc, char const *argv[])
{
	Solution * s = new Solution();
	cout << s->wordPattern("abba","dog cat cat dog") <<endl;
	return 0;
}
