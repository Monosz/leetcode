class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result: List[bool] = []

        for candy in candies:
            result.append(all(candy + extraCandies >= c for c in candies))
        
        return result
        