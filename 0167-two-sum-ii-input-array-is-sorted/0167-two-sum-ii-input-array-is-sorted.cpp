class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        int sum = numbers[left] + numbers[right];
        vector<int> res;

        // take advantage of the fact that the list is increasing order
        while(sum != target){
            if(sum < target) left++; // guaranteed to increase sum
            else if(sum > target) right--; // guaranteed to decrease sum
            sum = numbers[left] + numbers[right];
        }
        
        res.push_back(left + 1);
        res.push_back(right + 1);
        
        return res;
    }
};