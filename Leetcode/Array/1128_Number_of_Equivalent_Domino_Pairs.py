from collections import defaultdict
def numEquivDominoPairs(dominoes) -> int:
    result = 0
    maps = defaultdict(int)

    for num in dominoes:
        sortedNum = tuple(sorted(num))
        result += maps[sortedNum]
        maps[sortedNum] += 1

    return result
    # result = 0
    # for i in range(len(dominoes)):
    #     a, b = dominoes[i]
    #     if a > b:
    #         dominoes[i] = [b, a]

    # for i in range(len(dominoes)):
    #     for j in range(i+1, len(dominoes)):
    #         if dominoes[i] == dominoes[j]:
    #             result += 1
    
    # return result
            