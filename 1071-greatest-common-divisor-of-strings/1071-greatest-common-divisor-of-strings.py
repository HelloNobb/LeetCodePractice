class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 같은 반복주기로 생긴 문자열인지 확인
        if (str1 + str2 != str2 + str1):
            return ""
        
        # 두 문자열 길이의 최대공약수 구하기
        len1 = max(len(str1), len(str2))
        len2 = min(len(str1), len(str2))

        def get_gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
        cycle = get_gcd(len1, len2)
        rslt = str1[:cycle]
        return rslt
        
