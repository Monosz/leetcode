class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and len(flowerbed) == 1:
                    flowerbed[i] = 1
                    n -= 1
                elif i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n == 0:
                return True
        return False
        