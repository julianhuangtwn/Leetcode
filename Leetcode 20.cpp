/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

*/


#include <stack>

class Solution {
public:
    bool isValid(string s) 
    {
        bool valid = true;
        
        //Creates a stack, which is a sort of LIFO array that can be easily manipulated with predefined methods
        stack<char> bracketStack;
        
        //As s is a string type, to loop through all characters of a string we use this notation
        for (char bracket : s)
        {
            if (bracket == '(' || bracket == '[' || bracket == '{')
            {
                //Adds the bracket char to the "top" of the stack. The top is not referring to index 0, it's the most recently "in" character
                bracketStack.push(bracket);
            }

            else
            {
                //First checks if stack is empty, or else an error would occur trying to access empty stack
                //Then matches the found non-opening bracket to the most recently pushed bracket
                if (!bracketStack.empty() && 
                    ((bracketStack.top() == '(' && bracket == ')')
                   || (bracketStack.top() == '[' && bracket == ']')
                    || (bracketStack.top() == '{' && bracket == '}'))
                   )
                {
                    //pop removes the top element of the stack (the last in object)
                    bracketStack.pop();
                }
                //If stack is empty while an opening bracket is found, s is invalid
                else
                {
                    valid = false;
                }
            }
        }
        //If at the end of the string the stack isn't empty, s is invalid
        if (!bracketStack.empty())
        {
            valid = false;
        }

        return valid;
    }
};




/*There are several cases to consider for this question. A simple () could be simply matched with the next element for when you find an opening bracket, and if they don't match then s is invalid. This way works with the provided example testcases, however, in cases where we have nested brackets such as {()}, This way of checking the next element doesnt work. We see that in this case, the last opening bracket should be checked for a closing bracket. If let's say we have {()}[], we need () to be resolved first, then followed by {}, lastly []. So, by utilizing a stack, where it operates on the principle of Last In First Out, we go through the string character by character. Each time we encounter an opening bracket, we add it to the stack, hence it becomes the last in (top of the stack). Then, everytime there isn't an opening bracket, we match it with the corresponding top bracket. If there is a match, we remove that openint bracket from the list, allowing the next bracket to be matched. Anytime a closing bracket cannot be matched, or that there is something left over in the stack at the end of the string, the string is invalid*/