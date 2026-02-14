'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num = len(candies)
        rslt = [True] * num
        
        for i in range(num):
            new = candies[i] + extraCandies

            for j in range(num):
                if new < candies[j]:
                    rslt[i] = False
                    break
            
        return rslt
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find max
        maxCandies = max(candies)

        # find if target
        rslt = [False]*len(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                rslt[i] = True
        
        return rslt