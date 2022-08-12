class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result;
        int counter;
        for(int i=0;i<=n;i++)
        {
            counter = countOnes(i);
            result.push_back(counter);
        }
        return result;
    }
    
private:
    int countOnes(int n){
        if(n<2) return n; // Base case if n=0 or n=1
        
        // Binary works in powers of 2's so:
        if(n%2 == 0) return countOnes(n/2); // Even case
        return 1 + countOnes(n/2); // Odd case since all odd numbers will have the extra 1, not being divisible by 2
    }
};