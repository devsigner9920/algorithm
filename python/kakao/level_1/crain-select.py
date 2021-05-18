def solution(board, moves):
    answer = 0

    temp_stack = []

    for move in moves:
        for i in range(len(board)):
            item = board[i][move - 1]
            if item == 0:
                continue

            if len(temp_stack) == 0:
                temp_stack.append(item)
            else:
                pop_data = temp_stack.pop()
                if item == pop_data:
                    answer += 2
                else:
                    temp_stack.append(pop_data)
                    temp_stack.append(item)
            board[i][move - 1] = 0
            break

    return answer


print(
    solution([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ],
        [1, 5, 3, 5, 1, 2, 1, 4])
)
