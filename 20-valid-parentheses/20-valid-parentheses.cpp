#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(int i=0;i<s.size();i++) // For each character
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') stack.push(s[i]); // If it's an opening parentheses add it to the stack
            else
            {
                if (stack.empty()) return false; // Edge case where no opening parentheses was ever added to the stack
                
                // If the parenthese don't match to their correct counterpart
                if((stack.top() == '(' && s[i] != ')') || (stack.top() == '{' && s[i] != '}') || (stack.top() == '[' && s[i] != ']')) return false; // By clause 2
                
                stack.pop(); // If the next character is a valid closing one that matches it's opening counterpart in the correct order
            }
        }        
        return stack.empty(); // Stack should be empty if the string was valid
    }
};