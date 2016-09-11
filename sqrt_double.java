import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class Solution {
  double sqrt(int num){
      int int_part = sqrt_int(num);
      double res = int_part * int_part; // get the integer part
      double decimal_part = num - res;
      if(decimal_part == 0)
          return int_part;
      // if there is residue calculate the decimal part
      int start = 1;
      int end = 99;
      while(start + 1 < end){
          int mid = (start + end)/2;
          double decimal = (mid+0.0)/100;
          res = (int_part + decimal) * (int_part + decimal);
          if(res < num)
              start = mid;
          if(res > num)
              end = mid;
      }
      double decimal_start = (start+0.0)/100;
      double decimal_end = (end+0.0)/100;
      double num1 = (int_part + decimal_start) * (int_part + decimal_start);
      double num2 = (int_part + decimal_end) * (int_part + decimal_end);
      return Math.abs(num1-num) > Math.abs(num2 - num)?(int_part + decimal_end):(int_part + decimal_start);
  }
  int sqrt_int(int num){
      if(num <= 0) return 0;
      int start = 1;
      int end = num;
      long  res = 0;
      while(start + 1 < end){
          int mid = start + (end-start)/2;
          res = mid * mid;
          if(res == num)
              return mid;
          if(res < num)
              start = mid;
          else
              end = mid;
      }
      res = end * end;
      if(res == num)
          return end;
      return start;
  }
  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.sqrt(2));
  }
}
