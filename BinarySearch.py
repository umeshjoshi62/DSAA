https://leetcode.com/problems/binary-search/editorial/
  
  class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums)-1

        # while (l <= r ):
        #     mid  = (r + l) // 2
        #     #print("({} + {})//2={}".format(r,l,mid))
        #     # print(nums[mid])
        #     if target < nums[mid] :
        #         r = mid - 1  
        #     elif target > nums[mid] :
        #         l = mid + 1
        #     elif target == nums[mid]:
        #         return mid
        # return -1
        return self.dfs(nums,target,0,len(nums)-1)


    def dfs(self,nums,target,start,end):
        if start > end :
            return -1
        mid = (start + end ) // 2
        if target < nums[mid]:
            print(mid)
            return self.dfs (nums,target,start,mid-1)
        elif target > nums[mid]:
            return self.dfs (nums,target,mid+1,end)
        elif target == nums[mid] :
            return mid
        



