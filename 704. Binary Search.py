# https://leetcode.com/problems/binary-search/

class Solution(object):
  
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid =(left+right)/2
        index = -1
        
        while left <= mid:
            
            if nums[mid] == target:
                index = mid
                break

            elif nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            mid = (left + right)/2    

        return index