class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        amount = len(s)
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        rsltV = []

        for i in range(amount):
            if s[i] in vowels:
                rsltV.append(i)
        
        for i in range(len(rsltV)//2):
            idx1 = rsltV[i]
            idx2 = rsltV[len(rsltV)-1 - i]
            s[idx1], s[idx2] = s[idx2], s[idx1]

        
        return "".join(s)

'''
### 조건
---
- 길이: 1 ~ 30만

### 접근 계획
---
방법 1)
[ 좌 포인터, 우 포인터 잡고 서로가 같아질때까지 한칸씩 이동하며 하나씩 모음 잡고 바꾸기 ]
0: 모음 배열을 만든다. _ ['a','e','i','o','u','A','E','I','O','U']
1: string 길이의 절반값을 구한다. _ len(str)/2
2: 

방법 2)
[ 반복문 1회 쭉 돌려 인덱스-모음글자 쌍의 딕셔너리 만들고 마지막에 좌우 쌍 인덱스로 전부 바꾸기 ]
0: 
'''