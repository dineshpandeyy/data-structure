'''
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]


length = 10
updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]
'''

def rangeAddition(length, updates):
    array = [0] * length

    for update in updates:
        start = update[0]
        end = update[1]
        value = update[2]

        array[start] += value

        if end + 1 < length:
            array[end+1] -= value

    summ = 0
    for i in range(len(array)):
        summ += array[i]
        array[i] = summ
    
    return array

length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print(rangeAddition(length, updates))


length = 10
updates = [[2,4,6],[5,6,8],[1,9,-4]]
print(rangeAddition(length, updates))

    
    