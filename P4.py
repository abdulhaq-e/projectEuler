def palindrome(n):

    palin = []
    for i in range(999,100,-1):
        for j in range(999, 100, -1):
            x = i * j
            if str(x)[::-1] == str(x):
                palin.append(x)
    return max(palin)
            
