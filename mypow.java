public class Solution {
    public double myPow(double x, int n) {
        if(n == 0) return 1;
        if(n == 1) return x;
        boolean neg = false;
        if(n < 0){
            neg = true;
            n = -n;
        }
        double half = myPow(x,n/2);
        double res = half*half*myPow(x,n - (n/2)*2);
        if(neg){
            if(res == 0)
                return 0;
            return 1/res;
        }
        return res;
    }
}