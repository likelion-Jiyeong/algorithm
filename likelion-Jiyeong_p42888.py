def solution(records):
    res_arr = []
    dict = {}
    dict_id = {}
    for idx, val in enumerate(records):
        temp = val.split()
        dict_id[temp[1]] = temp[-1]
        if "Enter" in val:
            msg = temp[1]+"님이 들어왔습니다."
        elif "Leave" in val:
            msg = temp[1]+"님이 나갔습니다."
        
        dict[idx] = msg
    print(f"dict_id >> {dict_id}")
    print(f"dict >> {dict}")
    
    for key,value in dict.items():
        id = value.split('님')
        print(f"id >>{id[0]}")
        mes = dict_id[id[0]]+id[1]
        print(f"mes >> {mes}")
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

