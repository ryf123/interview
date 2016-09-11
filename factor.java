public class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> ret = new ArrayList();
        ArrayList<Integer> path = new ArrayList();
        traverse(ret,path,n,2);
        return ret;
    }
    void traverse(List<List<Integer>> ret,ArrayList<Integer> path,int n,int start){
        if(path.size() >= 1){
            path.add(n);
            ret.add(new ArrayList(path));
            path.remove(path.size()-1);
        }
        for(int i=start;i<=Math.sqrt(n);i++){
            if(n%i == 0){
                path.add(i);
                traverse(ret,path,n/i,i);
                path.remove(path.size()-1);
            }
        }
    }
}