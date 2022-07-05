import re
def solution(text):
    text = text.lower() # 소문자변환
    print(f"text >> {text}")   
    re.sub(r'[^a-z0-9-_.]','',text)
    print(f"text >>{text}")
solution('AbcD**')