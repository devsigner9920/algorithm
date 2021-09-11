import math

LAST_TIME = 23 * 60 + 59


def get_min(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])


def solution(fees, records):
    answer = []
    in_cars = {}
    adj_time = {}
    for record in records:
        car_info = record.split()
        if car_info[2] == 'IN':
            in_cars[car_info[1]] = get_min(car_info[0])
            if car_info[1] not in adj_time:
                adj_time[car_info[1]] = 0
        else:
            adj_time[car_info[1]] += get_min(car_info[0]) - in_cars[car_info[1]]
            in_cars.pop(car_info[1])
    for exist_car in in_cars:
        adj_time[exist_car] += LAST_TIME - in_cars[exist_car]

    print(adj_time)
    for car in sorted(adj_time):
        minute = adj_time[car]
        if minute <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((minute - fees[0]) / fees[2]) * fees[3]))
    return answer


solution([1, 461, 1, 10],
         ["00:00 1234 IN"])
