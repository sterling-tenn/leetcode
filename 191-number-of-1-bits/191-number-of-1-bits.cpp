class Solution {
public:
    int hammingWeight(uint32_t n) {
        if(n == 0) return 0;
        
        int counter = 0;
        for(int i = 0; i < 32; i++) // uint32_t is 32 bits long
        {
            auto tmp = (n >> i) & 1; // Bit shift the number right i number of times(to check the ith iteration bit), then AND it with 1 so verify it's value
            if(tmp == 1) counter++;
        }
        return counter;
    }
};