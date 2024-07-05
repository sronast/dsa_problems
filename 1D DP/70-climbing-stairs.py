class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        a =1 
        b = 2
        i =2
        while i<n:
            temp = b
            b = a+b
            a = temp
            i+=1
        return b


#### cpp soln#####
# class Solution {
# public:
#     int climbStairs(int n) {
#         int a = 1;
#         int b= 2;
#         if (n==1 || n ==2){
#             return n;
#         }
#         for(int i=2;i<n;i++){
#             int temp = b;
#             b = a+b;
#             a= temp;
#         }
#         return b;
        
#     }
# };