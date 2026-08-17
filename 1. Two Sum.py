class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums) :
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

solution = Solution()
print(solution.twoSum(nums = [3,3], target = 6))
