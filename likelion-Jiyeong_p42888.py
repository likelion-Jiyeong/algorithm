def solution(records):
    res_arr = []
    for idx, val in enumerate(records):
        temp = val.split()
        if "Enter" in val:
            msg = temp[-1]+"님이 들어왔습니다."
        elif "Leave" in val:
            msg = temp[1]+"님이 나갔습니다."
        res_arr.append(msg)
    print(f"res_arr >> {res_arr}")
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

