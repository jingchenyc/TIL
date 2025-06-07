class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            newSubsets = []
            for cur in output:
                temp = cur.copy()
                temp.append(num)
                newSubsets.append(temp)
            for cur in newSubsets:
                output.append(cur)
        return output
