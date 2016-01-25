#include "vector"
#include "queue"
#include "iostream"
#include "sstream"
using namespace std;
 // * Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
 	TreeNode *right;
 	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
    	if(root == NULL){
    		return "";
    	}
    	string ret = to_string(root->val);
    	queue<TreeNode*> queue;
    	queue.push(root);
    	while(queue.size()){
    		TreeNode* node = queue.front();
    		queue.pop();
    		if(node->left){
    			ret += ","+to_string(node->left->val);
    			queue.push(node->left);
    		}
    		else{
    			ret += ",#";
    		}
    		if(node->right){
    			ret += ","+to_string(node->right->val);
    			queue.push(node->right);
    		}
    		else{
    			ret += ",#";
    		}    		
    	}
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size() == 0){
        	return NULL;
        }
    	vector<string> data_array;
    	queue<TreeNode*> queue;
    	int pos = 0;
        for (int i = 0; i < data.size(); ++i)
        {
        	if(data[i] == ','){
        		// cout<<data.substr(pos,i-pos)<<endl;
        		data_array.push_back(data.substr(pos,i-pos));
        		pos = i+1;
        	}
        }
        // cout<<data.substr(pos,data.size()-pos)<<endl;
        data_array.push_back(data.substr(pos,data.size()-pos));
        int start = 0;

        TreeNode* head = new TreeNode(stoi(data_array[start++]));
        queue.push(head);
        // cout<< head.val<<endl;
        while(queue.size() && start<data_array.size()){
        	TreeNode* node = queue.front();
    		cout<< node->val<<endl;
        	string leftval = data_array[start++];
        	if(leftval != "#" && start<=data_array.size()){
        		node->left = new TreeNode(stoi(leftval));
        		queue.push(node->left);
        	}
        	string rightval = data_array[start++];
        	if(rightval!= "#" && start<=data_array.size()){
        		node->right = new TreeNode(stoi(rightval));
        		queue.push(node->right);
        	}
        	// cout<<leftval<<data_array.size()<<start<<rightval<<endl;
        	queue.pop();

        }
        return head;
    }
};
int main(int argc, char const *argv[])
{
	Codec codec;
	TreeNode* oldhead = new TreeNode(1);
	// oldhead->left = new TreeNode(2);
	// oldhead->right = new TreeNode(3);
	cout<<codec.serialize(oldhead)<<endl;
	TreeNode* head =  codec.deserialize(codec.serialize(oldhead));
	cout<<head->val<<endl;
	// cout<<head->right->val<<endl;
	// cout<<head->left->val<<endl;
	return 0;
}
