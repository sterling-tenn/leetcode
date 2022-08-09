#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        unordered_map<char,int> map;
        
        map['I'] = 1;
        map['V'] = 5;
        map['X'] = 10;
        map['L'] = 50;
        map['C'] = 100;
        map['D'] = 500;
        map['M'] = 1000;
        
        for(int i = 0;i<s.size();i++)
        {
          if(map[s[i]] < map[s[i+1]]) // If the current value is less than the next one, we know that Roman numerals indicate that you're supposed to subtract the value instead of add it
          {
              sum -= map[s[i]];
          }
            else
            {
                sum += map[s[i]];
            }
        }
        return sum;
    }
};