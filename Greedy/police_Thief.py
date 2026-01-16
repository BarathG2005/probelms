# Police and Thieves
# Difficulty: MediumAccuracy: 34.03%Submissions: 57K+Points: 4
# Given an array arr[], where each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
# Keep in mind the following conditions :

# Each policeman can catch only one thief.
# A policeman cannot catch a thief who is more than k units away from him.
# Examples:

# Input: arr[] = ['P', 'T', 'T', 'P', 'T'], k = 1
# Output: 2
# Explanation: Maximum 2 thieves can be caught. First policeman catches first thief and second police man can catch either second or third thief.
# Input: arr[] = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2
# Output: 3
# Explanation: Maximum 3 thieves can be caught.


class Solution:
    def catchThieves(self, arr, k):
        #code here
        p = []
        t = []
        for i in range(len(arr)):
            if arr[i] == "P":
                p.append(i)
            else:
                t.append(i)
        i =0
        j =0 
        ans = 0
        while i<len(p) and j<len(t):
            if abs(p[i]-t[j])<=k:
                i+=1
                j+=1
                ans+=1
            elif p[i]<t[j]:
                i+=1
            else:
                j+=1
        return ans


# in this like the binary search 