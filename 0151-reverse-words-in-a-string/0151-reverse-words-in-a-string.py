class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1]) #뒤집기->공백무시 단어단위 자르기->공백단위합치기


''' ### 수동 풀이법 (2번 방식)
class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(s)

        words = []
        word = []
        for c in s:
            if c == " ": #공백이면 그 전까지 단어 하나로 합쳐 저장
                if word:
                    tmp = "".join(word)
                    words.append(tmp)
                word.clear()
            else:
                word.append(c)
        if word:
            tmp = "".join(word)
            words.append(tmp) #마지막 단어

        rev_words = words[::-1]
        rslt = " ".join(words[::-1])
        
        return rslt
'''

'''         
## 접근 계획
- 스택: ["하늘은", "매우", "파랗다"] -> 파랗다, 매우, 하늘은

1. 첫 글자~공백 전까지 하나의 리스트에 받아 합친다. (tmp = "하늘은")
2. 공백 마주치면 모아둔 문자열을 새 배열의 원소로 집어넣는다. (words = ['하늘은'])
==> 문자열 끝까지 반복 (words = ['하늘은', '매우', '파랗다'])
<방법1>
3. 역순으로 만들기 (words.reverse() # 파랗다, 매우, 하늘은)
4. 합치기
<방법2>
3. 스택처럼 pop() 이용해 끝 문자열부터 쭉 합치고 공백 넣기 (rslt = "하늘은 " + "매우 ")
4. 끝까지 반복, 끝 문자일 경우 마지막에 공백 넣지 않기
'''
