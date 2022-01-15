""""
LC #344 Reverse a String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.

Algorithm: 

1. Using a for loop, iterate through each character in the string array

2.  
"""

# Solution: 
# https://www.youtube.com/watch?v=5keS487q67M 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # declare two pointer variables: left and right
        left = 0;
        right = len(s) - 1
        # using a while loop, swap between the left and right pointers
        while left < right: 
        # store one of the pointers in a temporary variable named "tmp"
            tmp = s[left]
        # set value stored in left index equal to the value stored in right
            s[left] = s[right]
        # incremement left index by 1
            left += 1
        # set value stored in right index equal to value stored in tmp
            s[right] = tmp
        # decrement right index by 1
            right -= 1
        #s[left], s[right] = s[right], s[left]