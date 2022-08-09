class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSoFar = nums[0]; // Keep track of the current maximum subarray sum
        int maxEndingHere = nums[0]; // Keep track of the max ending at the prior index (for the loop)
        
        /*
        The idea is to compare the single current value at nums[i], with nums[i] + the previous maximum
        subarray value (maxEndingHere)
        */
        for(int i=1; i<nums.size();i++)
        {
            maxEndingHere = std::max(maxEndingHere + nums[i], nums[i]); // The max ending at the index is either itself, or itself plus the max of the previous index
            maxSoFar = std::max(maxSoFar,maxEndingHere); // Update the possible max value
        }
        return maxSoFar;
    }
};