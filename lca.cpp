// *
//  * Definition for a binary tree node.
#include <iostream>
using namespace std;

struct TreeNode {
	int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {

    }
};
 
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    	if(root == NULL){
    		return NULL;
    	}
    	if(root == p){
    		return p;
    	}
    	if(root ==q){
    		return q;
    	}
        TreeNode* left = lowestCommonAncestor(root->left,p,q);
        TreeNode* right = lowestCommonAncestor(root->right,p,q);
        if(left != NULL and right != NULL){
        	return root;
        }
        else if(left != NULL and right == NULL){
        	return left;
        }
        else{
        	return right;
        }
    }
};
int main(int argc, char const *argv[])
{
	TreeNode root = TreeNode(1);
	TreeNode right = TreeNode(2);
	TreeNode left = TreeNode(3);
	root.right = &right;
	root.left = &left;
	Solution s;
	TreeNode* ret = s.lowestCommonAncestor(&root,&left,&right);
	cout<<ret->val<<endl;
	return 0;
}