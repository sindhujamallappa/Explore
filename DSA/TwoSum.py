'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {} #Initializes an empty dictionary, maps each number (num) to its index in nums, to quickly check if a complement exists
        for i, num in enumerate(nums):
            print(f"i-{i} num-{num}")
            diff = target - num
            print("Difference: " + str(diff) )
            if diff in num_map:
                return [num_map[diff], i]
            num_map[num] = i

solution = Solution() # Instance of class Solution - solution is the object of Solution()
run = solution.twoSum([2,7,11,15], 9) #Calling the method of the created object
print(run)
'''
Parameters:
nums: a list of integers (the input array).
target: the integer target sum.

Returns:
A list of two indices whose corresponding numbers in nums add up to target.

'''