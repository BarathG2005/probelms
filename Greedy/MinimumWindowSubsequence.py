# You are given two strings, s1 and s2. Your task is to find the smallest substring in s1 such that s2 appears as a subsequence within that substring.

# The characters of s2 must appear in the same sequence within the substring of s1.
# If there are multiple valid substrings of the same minimum length, return the one that appears first in s1.
# If no such substring exists, return an empty string.
# Note: Both the strings contain only lowercase english letters.

# Examples:

# Input: s1 = "geeksforgeeks", s2 = "eksrg"
# Output: "eksforg"
# Explanation: "eksforg" satisfies all required conditions. s2 is its subsequence and it is smallest and leftmost among all possible valid substrings of s1.
# Input: s1 = "abcdebdde", s2 = "bde" 
# Output: "bcde"
# Explanation:  "bcde" and "bdde" are two substring of s1 where s2 occurs as subsequence but "bcde" occur first so we return that.
# Input: s1 = "ad", s2 = "b" 
# Output: ""
# Explanation: There is no substring exists.
# Constraints:
# 1 ≤ s1.length ≤ 104

class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n = len(s1)
        m = len(s2)
        mi = float('inf')
        st = 0
        i =0
        while i<n:
            j = 0
            while i<n:
                if s1[i] == s2[j]:
                    j+=1
                    if m == j:
                        break
                i+=1
            if j>m or i>=n:
                break
            
            end= i
            j = m-1
            # print(s1[i],i)
            while i>0:
                # print(s1[i],s2[j],i,j)
                if s1[i] == s2[j]:
                    j-=1
                    if j<0:
                        break
                i-=1
            # print(s1[i],i)
            # st = i
            if (end-i+1)<mi:
                mi = end-i+1
                st = i
                # print(s1[st:end+1])
            i+=1
            
        return "" if mi == float('inf') else s1[st:st+mi]
                    
                
# Two pointers approach is used here.
#goo find the forword and find the backword
