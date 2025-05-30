"""
입력 : n명의 출근지정 날짜, 실제 일주일동안 출근했던 시간, 
출력 : workday기준 5일 모두 지각 안한 인원
조건 : 주말은 빼야한다, 시작은 start 기준으로 잡아야한다.
day가 6, 7 이면 빼야한다
시간은 시간 * 100 + 분으로 나타낸다.
시간
비교를 위해서는 분으로 모두 수정해야한다.
7시 10분 -> 60  * 7 + 10
timelog가 10 이상 이면 안된다.
전체적으로 for schedules : for 

"""
def change_minutes(time):
    hour = time // 100
    minutes = time % 100
    return hour * 60 + minutes

def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        count = 0
        for j in range(len(timelogs[i])):
            day = ((startday - 1) + j) % 7 + 1
            if day == 6 or day == 7: # 주말 처리
                continue
            on_minutes = change_minutes(schedules[i])
            total_minutes = change_minutes(timelogs[i][j])
            if total_minutes - on_minutes <= 10:
                count += 1
        if count == 5:
            answer += 1

    return answer

schedules = [730, 855, 700, 720]
timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
startday = 1

answer = solution(schedules, timelogs, startday)
print(f"answer >> {answer}")