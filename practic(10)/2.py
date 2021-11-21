def activity_selector(activity: list) -> list:
    assert type(activity) == list, 'type(activity) != list'

    activity.sort(key=lambda x: x[1])
    results = [activity[0]]

    def selector(k: int) -> None:
        m = k + 1
        while m < len(activity) and activity[m][0] < activity[k][1]:
            m += 1
        if m < len(activity):
            results.append(activity[m])
            results.append(selector(m))

    selector(0)
    return list(filter(lambda x: x != None, results))

print(activity_selector([
    (0, 80), (0, 9), (0, 80), (10, 15), (4, 59), (15, 94), (15, 24), (25, 46), (46, 96)
]))