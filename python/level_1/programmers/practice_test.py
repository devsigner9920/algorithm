def solution(answers):
    answer = []
    forgive_1 = [i for i in range(1, 6)]
    forgive_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    forgive_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    answer_1 = 0
    answer_2 = 0
    answer_3 = 0

    for ans in answers:
        if ans == forgive_1[cnt_1]:
            answer_1 += 1
        if ans == forgive_2[cnt_2]:
            answer_2 += 1
        if ans == forgive_3[cnt_3]:
            answer_3 += 1

        if cnt_1 == len(forgive_1) - 1:
            cnt_1 = 0
        else:
            cnt_1 += 1

        if cnt_2 == len(forgive_2) - 1:
            cnt_2 = 0
        else:
            cnt_2 += 1

        if cnt_3 == len(forgive_3) - 1:
            cnt_3 = 0
        else:
            cnt_3 += 1

    max_answer = max(answer_1, answer_2, answer_3)
    if max_answer == answer_1:
        answer.append(1)
    if max_answer == answer_2:
        answer.append(2)
    if max_answer == answer_3:
        answer.append(3)

    return answer