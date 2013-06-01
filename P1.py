def factors(n1, n2, m):
    '''n is the number, m is the range'''
    f = [x for x in xrange(1,m) if (x%n1 == 0) or (x%n2 == 0)]
    return f

def sumOfFactors(n1,n2,m):
    f = factors(n1, n2, m)
    
    #print f1
    ans = sum(f)
    return ans


'''
that was my solution, the first solution in the pdf gives the same however,
there's a chance of an integer overflow if m is say, 10,000,000,000,000
so a better solution to find the sum of the factors of 5 and the sum of the
factors of 3 and subtract from them the sum of the factors of 15 (to delete
repeated factors)

3 + 6 + 9 + 12 + 15 + ... + 999 = 3*(1+2+3+4+5+6+...+333)

5 + 10 + 15 + ... + 995 = 5*(1+2+3+4+...+195)

the rule from summing 1+2+3+4+...+p is given by the famous (probably false)
story of Gauss in the classroom.

1+2+3+4+...+p = 0.5*p*(p+1)
'''

def sumOfFactors2(n, m):
    p = (m-1) / n #this will give an integer as long as n and m are.
    print p
    summation = n*p*(p+1)/2

    return summation

def solution2(n1, n2 ,m):
    n3 = n1 * n2

    return sumOfFactors2(n1,m) + sumOfFactors2(n2,m) - sumOfFactors2(n3,m)
