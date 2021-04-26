# Leetcode_Running_Sum

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example:

```Python
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
```

```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:  
```
---

I've come across this question before while learning javascript, and while Python does have a reduce function I wanted to approach this without importing any tools.


```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newArr = [] # Results go here
        for n, value in enumerate(nums): # Loop through our input
```

The expected output is an array, so we first setup an array that is going to store our results(newArr), a for loop is also required to iterate through our input. Together with the built-in enumerate function, a set of steps can be applied to each index of the input array defined as 'nums'. The current index will be represented by 'n', and 'value' will represent the stored value at that index. 

```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newArr = [0]
        for n, value in enumerate(nums):
            newArr.append(newArr[n] + value)
            
        return newArr[1:]
```

The goal is to continuously add the next value of our input array to the previous value, and append the result to 'newArr'. This can be accomplished by taking the sum of the current value at index 'n' in newArr, with 'value' from the 'nums' array. However, the loop will not execute while 'newArr' is empty, so we add a '0' at the first index. When the loop completes, we slice newArr to ignore the first index.

```Python
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

# 1st Iteration
newArr[n] = 0 # 1st Index of newArr, 0
value = nums[n] # 1st Index of nums, 1
newArr.append(newArr[n] + value) # Appends sum of 0 + 1 to newArr as 2nd index

# 2nd Iteration
newArr[n] = 1 # 2nd Index of newArr, result of previous append, 1
value = nums[n] # 2nd Index of nums = 2
newArr.append(newArr[n] + value) # Appends sum of 1 + 2 to newArr as 3rd index

etc...
```

The final result is a running sum of the previous indices!

```Python

nums = [1,2,3,4]

runningSum(nums)

# [0+1, 1+2, 3+3, 6+4]
# Returns [1,3,6,10]
```



