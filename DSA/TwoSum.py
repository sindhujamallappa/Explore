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
        print(f"Initialised empty dictionary: {num_map}")
        for i, num in enumerate(nums): #for each value in the input array
            print(f"Current value i: {nums[i]}, searching for difference {target-num}")
            diff = target - num #Check if the targe - current number value ie is the difference number present
            if diff in num_map:
                print(f"Difference number: {diff} found at position: {num_map[diff]}")
                return [num_map[diff], i]
            num_map[num] = i
            print(f"Difference number not found, Current dictionary: {num_map}")

solution = Solution() # Instance of class Solution - solution is the object of Solution()
run = solution.twoSum([15,12,7,2], 9) #Calling the method of the created object
print(run)

#Time Complixity: The main thing to notice is that we loop through the list once, and each lookup in the hash map is instant (constant time). So, if there are n numbers, we do operations. That’s O(n) time.

'''
Parameters:
nums: a list of integers (the input array).
target: the integer target sum.

Returns:
A list of two indices whose corresponding numbers in nums add up to target.
'''