# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 06:23:58 2023

@author: neelu
"""
"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c = combinations(nums,3)
        lst = []
        for j in c:
            name = sorted(list(j))
            if sum(name) == 0:
                if name not in lst:
                    lst+=[name]
                else:
                    continue
        return lst