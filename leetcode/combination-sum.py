class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def dfs(i, currSum):
            if currSum == target:
                res.append(sol.copy())
                return
            
            if i >= len(candidates) or currSum > target:
                return
            
            sol.append(candidates[i])
            dfs(i, currSum + candidates[i])

            sol.pop()
            dfs(i + 1, currSum)
        
        dfs(0, 0)
        return res