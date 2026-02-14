class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        # 접근법
        - 걍 완탐
        '''
        num = len(candies)
        rslt = [True] * num
        
        for i in range(num):
            new = candies[i] + extraCandies

            for j in range(num):
                if new < candies[j]:
                    rslt[i] = False
                    break
            
        return rslt