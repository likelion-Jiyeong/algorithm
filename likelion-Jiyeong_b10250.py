def get_room_number(w,h,n): 
    c = h//n + 1
    d = h % n
    if d == 0:
        c = h//n
        d = n
    return d*100+c


def main():
    _input = int(input())
    for case in range(_input):
        w,h,n = map(int, input().split())
        result = get_room_number(w,h,n)
        print(result)    

main()
