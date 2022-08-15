#include <stack>

class Solution {
public:
    bool isPalindrome(string s) {
        stack<char> stack; // Stack to compare since FIFO
        string alphanum;
        for(int i=0;i<s.size();i++)
        {
            // Append lowercase alphanumeric values
            if(isalnum(s[i]))
            {
                stack.push(tolower(s[i]));
                alphanum += tolower(s[i]);
            }
        }
        for(int i=0;i<alphanum.size();i++)
        {
            if(stack.top() != alphanum[i]) return false; // Compare from the start of the string to the end (the top of the stack)
            stack.pop(); // If control gets here then the front and end of the string match, go to the next from the front and next from the back
        }
        return stack.empty(); // If this is empty, all the pairs have matched and have been removed from the stack
    }
};