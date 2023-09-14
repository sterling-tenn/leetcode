class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        int difference;
        
        // Idea is to keep track of the values from the list and see if we can use them again in the future
        // Since hashmaps are O(1) we can constantly check of there's a number we can reuse
        for(int i = 0; i < nums.size(); i++){
            difference = target - nums[i]; // Difference required for this specific value
            
            // Have we seen a value before in the list with the difference that we need?
            if(hashmap.find(difference) != hashmap.end()){ // Number from the list is in the hashmap
                return vector<int>{i , hashmap[difference]};
            }
            hashmap.insert({nums[i] , i}); // Insert the number from the list and its corresponding index - (can we use this number again later?)
        }
        return {};
    }
};