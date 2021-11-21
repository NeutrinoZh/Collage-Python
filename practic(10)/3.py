def activity_selector(activity: list) -> list:
    assert type(activity) == list, 'activity must be a list'
    
    results = []
    n = len(activity)

    activity.sort(key=lambda x: x[1])

    i = 0
    results.append(activity[i])

    for j in range(1, n):
        if activity[j][0] >= activity[i][1]:
            results.append(activity[j])
            i = j

    return results

print(activity_selector([
    (0, 80), (0, 9), (0, 80), (10, 15), (4, 59), (15, 94), (15, 24), (25, 46), (46, 96)
]))