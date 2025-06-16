# 1432. Max Difference You Can Get From Changing an Integer
def maxDiff(num: int) -> int:
    s = str(num)

    maxStr = s
    for char in maxStr:
        if char != "9":
            maxStr = maxStr.replace(char, "9")
            break

    s = str(num)

    for i in range(len(s)):
        if i == 0 and s[i] != "1":
            s = s.replace(s[i], "1")
            break
        elif int(s[i]) > 0 and s[i] != s[0]:
            s = s.replace(s[i], "0")
            break
    
    return int(maxStr) - int(s)

    
num = 555      
print(maxDiff(num))