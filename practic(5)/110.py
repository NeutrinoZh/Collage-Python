# 15 (0,5)

def editDistance(str0, str1):
    if str0 == str1:
        return 0
    elif len(str0) == 0:
        return len(str1)
    elif len(str1) == 0:
        return len(str0)
    else:
        cost = 0
        if str0[-1:] != str1[-1:]:
            cost = 1

        d1 = editDistance(str0[:-1], str1)
        d2 = editDistance(str0, str1[:-1])
        d3 = editDistance(str0[:-1], str1[:-1])

        cost += min(d1, d2, d3)

        return cost

firstStr  = input('first string:\n')
secondStr = input('second string:\n')
print('edit distance:', editDistance(firstStr, secondStr))