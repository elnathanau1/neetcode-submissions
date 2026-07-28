class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(index: int, runningSum: int):
            if runningSum == target:
                results.append(subset.copy())
            for i in range(index, len(nums)):
                if nums[i] <= target - runningSum:
                    subset.append(nums[i])
                    dfs(i, runningSum + nums[i])
                    subset.pop()
        
        dfs(0, 0)

        return results

"""
3 4 5, 16

3 3
4
5


"""