class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        *-* 1/ 0
        *--* 2/ 0
        *---* 3/ 1
        *----* 4/ 1
        *-----* 5/ 2
        *------* 6/ 2
        *-------* 7/ 3
        ---* : *--*
        ----* : *-*-*
        -----* : *-*--* / -*-*-*

        # 접근계획
        1. 현재:
            - 심은 화분 -> 2칸 점프
            - 빈 화분 -> 다음 칸 비었으면 심기 -> 2칸 점프
        '''
        amount = len(flowerbed)
        point = 0
        maxNew = 0
        while (point < amount):
            if flowerbed[point] == 1:
                point += 2
            else:
                if point+1 >= amount:
                    maxNew+=1
                    flowerbed[point] = 1
                    break
                elif flowerbed[point+1] == 0:
                    maxNew += 1
                    flowerbed[point] = 1
                    point += 2
                else:
                    point += 3
        
        if maxNew >= n:
            return True
        return False