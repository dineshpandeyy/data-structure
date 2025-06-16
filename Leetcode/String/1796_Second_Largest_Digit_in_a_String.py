def secondHighest(s):
    res = []

    for char in s:
        if char.isdigit():
            res.append(int(char))
    
    res = list(set(res))
    if len(res) <= 1:
        return -1
    res.sort()
    return res[-2]