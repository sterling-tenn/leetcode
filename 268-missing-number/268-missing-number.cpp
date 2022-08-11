class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int result = 0;
        for(int i = 1;i<=n;i++) result += i; // Running sum of what the total sum should be
        for(int i = 0;i<n;i++) result -= nums[i]; // Subtract all the elements of the vector should leave the missing number
        return result;
    }
};