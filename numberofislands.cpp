#include "vector"
#include "iostream"
using namespace std;
class Solution {
public:
    int numIslands(vector<vector<char> >& grid) {
    	int count = 0;
    	int row = grid.size();
    	if(row==0){
    		return 0;
    	}
    	int col = grid[0].size();
    	// cout<<row<<col<<endl;
		for (int i = 0; i < row; ++i)
		    {
		    	for (int j = 0; j < col; ++j)
		    	{
		    		if(grid[i][j]=='1'){
		    			dfs(i,j,grid,row,col);
		    			count+=1;
		    		}
		    	}
		    }
    	return count;    
    }
    void dfs(int m,int n,vector<vector<char> >& grid,int row,int col){
    	grid[m][n] = '2';
    	if(m-1>=0 && grid[m-1][n] == '1'){
    		dfs(m-1,n,grid,row,col);
    	}
    	if(m+1 < row && grid[m+1][n] == '1'){
    		dfs(m+1,n,grid,row,col);
    	}
    	if(n-1>=0 && grid[m][n-1] == '1'){
    		dfs(m,n-1,grid,row,col);
    	} 
    	if(n+1<col && grid[m][n+1] == '1'){
    		dfs(m,n+1,grid,row,col);
    	}   
    }
};
int main(int argc, char const *argv[])
{
	Solution s;
	vector<vector<char> > matrix;
	vector<char> tmp;
	tmp.push_back('1');
	matrix.push_back(tmp);
	cout<<s.numIslands(matrix)<<endl;
	return 0;
}