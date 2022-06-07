#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#The tests are generated such that there is exactly one solution. You may not use the same element twice.

#Your solution must use only constant extra space.

#Example 1:
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

#Example 2:
#Input: numbers = [2,3,4], target = 6
#Output: [1,3]
#Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

#Example 3:
#Input: numbers = [-1,0], target = -1
#Output: [1,2]
#Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

#Algorithm
#We use two indices, pointing to the first and last element. Since the array is sorted in ascending order, choosing the indices w.r.t first and last elements 
#would cover the possibilities. Then we take the sum of these elements. If it is equal to target, then we got the only solution. If it is less than target, then we
#try the next possibility and increase the smaller index by 1. If it is greater than target, then we reduce the larger index by 1. Keep moving the indices, 
#until the solution is found.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      right = len(numbers)-1
      left = 0
      
      while right<=len(numbers):
        s = numbers[right] + numbers[left]
        
        if s == target:
          return [left+1, right+1]
        elif s < target:
          left += 1
        elif s > target:
          right -= 1
        
        
      
