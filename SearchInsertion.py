'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
nums contains distinct values sorted in ascending order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
'''

def search_insert(nums,target):
    # if target is in the list, index of target is returned.
    if target in nums:
        return nums.index(target)
    # if target is not in the list and is less than any number in the list, 
    # then index of number just greater than target is returned.
    else:
        for i in range(len(nums)):
            if target < nums[i]:
                return i
        # if target is not in the list and is greater than every element present in the list,
        # then one is added to the last index of the element of the list and is returned.
        return i+1 

print(search_insert([1,2,3,4],5))

 