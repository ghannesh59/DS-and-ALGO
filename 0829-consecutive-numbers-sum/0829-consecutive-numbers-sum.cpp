class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans=0;
        n=n*2;
        for(int i=1;i<=sqrt(n);i++){
            if(n%i==0){
                int x=i;
                int y=n/i;
                if(((x+y)%2==1) && ((y-x)%2==1)){
                    ans++;
                }
            }
        }
     return ans;   
    }
};