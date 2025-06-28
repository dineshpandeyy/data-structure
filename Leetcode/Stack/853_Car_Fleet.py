class Solution:
    def carFleet(target, position, speed):
        stack = []
        arr = []

        for pos, sped in zip(position, speed):
            arr.append([pos, sped])
        
        arr.sort()

        for pos, speed in arr[::-1]:
            time = (target-pos)/speed

            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)

        