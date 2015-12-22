#include <iostream>
#include "unordered_set"
#include "unordered_map"
#include "vector"
using namespace std;
class Solution {
public:
	unordered_map<string,bool> visited;
	vector<vector<string> > ret;
    vector<vector<string> > findLadders(string beginWord, string endWord, unordered_set<string> &wordList) {
    	bfs(beginWord,endWord,wordList);
    	return ret;
    }
    void bfs(string beginWord,string endWord,unordered_set<string> &wordList){
    	unordered_map<string,vector<vector <string> > > row;
    	unordered_map<string,bool> visited;
    	vector<string> firstrow;
    	firstrow.push_back(beginWord);
    	vector<vector <string> > tmp;
    	tmp.push_back(firstrow);
    	int lvl = 0;
    	row[beginWord] = tmp;
    	visited[beginWord] = true;
    	while(row.size() >0){
    		unordered_map<string,vector<vector <string> > > newrow;
    		unordered_set<string> thisrowvisited;
    		lvl++;
	        for (auto it:row)
	        {
	        	string word = it.first;
	        	string oldword = word;
	        	// cout<<oldword<<lvl<<endl;
	        	for (int i = 0; i < word.size(); ++i)
	        	{
	        		char oldchar = word[i];
		        	for (word[i]='a';word[i]<='z';++word[i]){
		        		if(word == endWord){
		        			vector<vector <string> > tmp = row[oldword];
		        			// cout<<word<<lvl<<oldword<<tmp.size()<<endl;
			        			for(vector<string> tmptmp:tmp){
			        				tmptmp.push_back(word);
			        				ret.push_back(tmptmp);
		        			}
		        			continue;
		        		}
		        		if(word != oldword and visited.find(word) == visited.end()){
		        			if(wordList.find(word) != wordList.end()){
			        			vector<vector <string> > tmp = row[oldword];
			        			// cout<<word<<lvl<<oldword<<tmp.size()<<endl;
			        			for(vector<string> tmptmp:tmp){
			        				tmptmp.push_back(word);
			        				newrow[word].push_back(tmptmp);
			        			}
		        				thisrowvisited.insert(word);
		        			}
		        		}
		        	}
		        	word[i] = oldchar;
	        	}
	        }
	    	if(ret.size() > 0){
	    		break;
	    	}
	    	for(string tmp:thisrowvisited){
	    		visited[tmp] = true;	
	    	}
	    	row = newrow;
    	}
    }
};
int main(int argc, char const *argv[])
{
	Solution s;
	string beginWord = "red";
	string endWord = "tax";
	std::unordered_set<std::string> wordList ( {"ted","tex","red","tax","tad","den","rex","pee"} );
	for(auto v:s.findLadders(beginWord,endWord,wordList)){
		for (string word:v){
			cout<<word<<endl;
		}
	}
	// beginWord = "a";
	// endWord = "c";
	// wordList =  {"a,b,c"};
	// for(auto v:s.findLadders(beginWord,endWord,wordList)){
	// 	for (string word:v){
	// 		cout<<word<<endl;
	// 	}
	// }
	return 0;
}