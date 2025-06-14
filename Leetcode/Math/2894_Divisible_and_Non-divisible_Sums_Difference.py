def differenceOfSums(self, n: int, m: int) -> int:
    notDiv = 0
    div = 0

    for i in range(1,n+1):
        if i % m != 0:
            notDiv += i
        else:
            div += i
    
    return notDiv - div