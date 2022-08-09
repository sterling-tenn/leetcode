class Solution {
public:
    int getSum(int a, int b) {
        unsigned int carry; // Unsigned int because it's shifted later
        while(b != 0)
        { // Bitwise operations: Add the sum and the carry together by shifting the carry left once
            carry = a & b; // AND bitwise operator to get the carry value
            a = a ^ b; // XOR bitwise operator for the sum
            b = carry << 1; // The new b value is the carry shifted left once
        } // Continue until the carry (b value) is zero
        return a;
    }
};