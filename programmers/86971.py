"""
입력 : wires 연결 정보
출력 : 가장 개수가 비슷한 분리된 두 송전탑에서 노드의 차이
해결방법
1 : 3
2 : 3

모든 경우의 수를 적용해보기
두개로 나눠지는 걸 어떻게 파악할 수 있는가?
(4, 3) -> 연결된 노드 가수 1, 2, 3 / 

"""

def solution(n, wires):
    answer = n # 최대 차이로 초기화
    graph = {}

    for wire in wires:
        if wire[0] not in graph:
            graph[wire[0]] = [wire[1]]
        else:
            graph[wire[0]].append(wire[1])

        if wire[1] not in graph:
            graph[wire[1]] = [wire[0]]
        else:
            graph[wire[1]].append(wire[0])

    # sorted_graph = sorted(graph.items(), key=lambda x: len(x[1]), reverse=False)
    # max_node_count = len(sorted_graph[-1][1])

    # max_nodes = [key for key, value in graph.items() if len(value) == max_node_count]
    
    def dfs(n, visited):
        visited[n] = True
        cnt = 1 # 자기 자신 포함
        for node in graph[n]:
            if not visited[node]:
                cnt += dfs(node, visited)
        return cnt
    
    for node in graph.keys():
        for i in graph[node]:

            # 임시로 wire 끊기
            graph[node].remove(i)
            graph[i].remove(node)

            visited = [False] * (n + 1)
            group_size = dfs(i, visited)
            diff = abs(group_size - (n-group_size))
            answer = min(diff, answer)

            graph[node].append(i)
            graph[i].append(node)          

    return answer

n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
answer = solution(n, wires)
print(f"answer >> {answer}")