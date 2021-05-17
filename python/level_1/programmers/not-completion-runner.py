import collections

def solution(participant, completion):
    # participant.sort()
    # completion.sort()

    # for p, c in zip(participant, completion):
    #     if p != c:
    #         return p
    
    # return participant.pop()

    a = collections.Counter(participant) - collections.Counter(completion)
    return list(a.keys())[0]
    
    


part = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]

print(solution(part, comp))