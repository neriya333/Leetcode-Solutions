# first version:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        length = len(nums)
        while (i+j < length):
            nums[i] = nums[i+j]
            while (i + j + 1 < length) and (nums[i] == nums[i+j+1]):
                j+=1
            i+=1
        return i

      
"""
ways to improve:

A) cleaner code is possable:
    
def removeDuplicate(self,nums: List[int]) -> int:
  j = 0
  for i in range(1, len(nums)):
    if nums[j] != nums[i]:
      j += 1
      nums[j] = nums[i]
   return j + 1

B) we can use the pop().

C) writing 
nums = sort(num) will allocate new memory but
nums[:] = sort(num) will not allocate new memory
  so i was told. why is that? mutability? 
  No. the reason is that a = b, make a point to b, or copy b
  while a[:] = b[:] <=> a[i] = b[i] for all i.
  cool.

D) creating a new repo in github is just by pretanding it exists: you give it a name and forwardslash.
"""
