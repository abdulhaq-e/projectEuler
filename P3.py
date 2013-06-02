def largestPrimeFactor(n):
    
    x = []
    for i in xrange(3, int(n**0.5)+1,2):
        if n%i == 0:
                x.append(i)
                n = n / i
        
        #print test
        #print all(test) == True
    return x

