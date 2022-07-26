def solution(strings, n):
    answer = []
    dict = {}
    temp= [x[n] for x in strings]
    for idx,val in enumerate(temp):
        dict[idx] = val
    
    dict_sort = sorted(dict.items(), key=lambda x: x[1])
    for i in dict_sort:
        answer.append(strings[i[0]])
    print(f"answer >> {answer}")
    return answer

solution(["abce", "abcd", "cdx"],2)