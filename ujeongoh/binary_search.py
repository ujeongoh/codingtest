class Solution:
    # 704. Binary Search
    def search(self, nums: List[int], target: int) -> int:
      left, right = 0, len(nums) - 1
      
      # 첫번째요소가 타겟보다 크거나 마지막요소가 타겟보다 작으면 -1 반환
      if nums[0] > target or nums[-1] < target:
          return -1

      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
              return mid
          elif nums[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      return -1 

    # 278. First Bad Version - isBadVersion()함수가 제공된다.
    def firstBadVersion(self, n: int) -> int:
      left, right, mid = 1, n, 0
      
      while left <= right:
          mid = (left + right) // 2

          # badversion이고 이전 요소가 badversion이 아니면 mid 반환
          if isBadVersion(mid):
              if not isBadVersion(mid - 1):
                  return mid
              right = mid - 1
          else:
              left = mid + 1
      return mid

    # 35. Search Insert Position
    def searchInsert(self, nums: List[int], target: int) -> int:
      left, right, mid = 0, len(nums) - 1, 0
      
      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
              return mid
          elif nums[mid] > target:
              right = mid - 1                
          else:
              left = mid + 1
      # 같은 값이 없을 경우 left 반환
      return left