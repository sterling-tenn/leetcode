class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t sum = 0; // Running sum
        int exp = 31; // Start the 2^exp at 31 (not 0) since we're reversing the value of binary
        for(int i=0;i<32;i++)
        {
            auto tmp = (n >> i) & 1; // Scan each value of the binary value from right to left
            if(tmp == 1) sum += pow(2,exp); // Add the proper value if it's 1
            exp--; // Decrement the exponent for the next digit
        }
        return sum;
    }
};