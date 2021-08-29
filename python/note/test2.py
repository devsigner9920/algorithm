# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T, R):
    test = set(list(map(lambda x: x[:-1] if x[-1].isalpha() else x, T)))
    ok_score = int(100 / len(test))

    print(ok_score)

    for i in range(len(T)):
        if T[i][-1].isalpha():
            if R[i] != 'OK':

                test.discard(T[i][:-1])
        else:
            if R[i] != 'OK':
                test.discard(T[i])
    return int(ok_score * len(test))










solution(['test1a', 'test2', 'test1b', 'test1c', 'test3'], ['Wrong answer', 'OK', 'Runtime error', 'OK', 'Time limit exceeded'])