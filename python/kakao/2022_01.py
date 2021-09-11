def solution(id_list, report, k):
    answer = []
    reporter = {id: 0 for id in id_list}
    reported_count = reporter.copy()
    report_target = {id: [] for id in id_list}

    for item in report:
        repo = item.split()

        if repo[1] not in report_target[repo[0]]:
            reported_count[repo[1]] += 1
            report_target[repo[0]].append(repo[1])

    for repo in report_target:
        for item in report_target[repo]:
            if reported_count[item] >= k:
                reporter[repo] += 1

    answer = list(reporter.values())

    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
