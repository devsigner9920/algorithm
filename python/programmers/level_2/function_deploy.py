import math

def solution(progresses, speeds):
    answer = []

    while len(progresses):
        chk = 1
        cur_prog =progresses.pop(0)
        cur_speed =speeds.pop(0)
        finish_day = math.ceil((100 - cur_prog) / cur_speed)
        
        while len(progresses):
            comp_prog = progresses[0] + finish_day * speeds[0]
            if comp_prog >= 100:
                progresses.pop(0)
                speeds.pop(0)
                chk += 1
            else:
                break
        answer.append(chk)

# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer
        



    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))