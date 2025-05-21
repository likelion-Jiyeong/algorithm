class Solution:
    """
    for문을 여러 번 사용하거나 순열, 조합 라이브러리를 활용하고 싶으면 백트래킹을 고려해보기!
    digits의 길이가 0이면 return []
    dfs 함수()
    # 조건 - 조합되는 문자열의 길이는 digits와 같아야함 -> 이 경우 더 탐색 없이 저장 후 되돌아감
    if 현재 digit index가 입력받은 문자열 길이와 같으면
    문자 조합 저장 및 반환
    digits, 현재 인덱스 + 1, dic, 지금까지의 문자 조합 + 문자, 결과 리스트
    """
    def letterCombinations(self, digits: str) -> list[str]:
        answer = []

        phone_map: dict = {
            2: 'abc', 3: 'def',
            4: 'ghi', 5: 'jkl', 6: 'mno',
            7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }

        if len(digits) == 0:
            return []
        
        

        def dfs(self, i, curStr):
            if len(digits) == len(curStr):
                answer.append(curStr)
                return
            
            for str in phone_map[digits[i]]:
                dfs(i+1)
        
        return answer
    
solution = Solution()
digits = "23"
solution.letterCombinations(digits)