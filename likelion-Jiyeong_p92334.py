def solution(id_list, report, k):
    answer = []
    map_list = {}
    for idx, cont in enumerate(report):
        cont_split = cont.split(' ')
        map_list[cont_split[0]] = cont_split[1]
        print(f"map_list >> {map_list}")
    return answer

solution()