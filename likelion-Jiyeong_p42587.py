def solution(prior,loc):
    # prior 정렬
    max = 0
    max_idx = 0
    wait_arr = []
    while prior:
        for idx, val in enumerate(prior):
            if idx == len(prior):
                max_idx = idx
            else:
                if val > max:
                    max = val
                    max_idx = idx
            prior.pop(max_idx) #prior에서 max_idx번째 요소를 삭제
            print(f"prior >> {prior}")
            wait_arr.append(max_idx)
            print(f"wait_arr >> {wait_arr}")    
                
solution([2,1,3,2],2)