class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(index: int):
            if index >= len(nums):
                results.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return results


"""
results = [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]    
subset = []
nums = [1,2,3]

f(0) -> f(1) -> f(2) -> f(3)
                     -> f(3)
             -> f(2) -> f(3)
                     -> f(3)
     -> f(1) -> f(2) -> f(3)  
                     -> f(3)   
             -> f(2) -> f(3) 
                     -> f(3)         

"""