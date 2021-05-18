def solution(num):
    sol_arr = []
    stop = 0
    sol = num

    if 1 <= sol <= 10 ** 6:
        while stop == 0:
            sol_arr.append(int(sol))
            sol = sol / 2 if sol % 2 == 0 else (sol * 3) + 1
            if sol == 1:
                sol_arr.append(int(sol))
                stop = 1

    return sol_arr


print(solution(138367))
