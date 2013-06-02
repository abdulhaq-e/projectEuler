def fibonaciGen1(n):
    
    x = [1,1]
    i = 0
    while x[-1] < n:
        x.append(x[i]+x[i+1])
        i += 1
    return x


def evenFib(n):
    
    return sum([x for x in fibonaciGen1(n) if x%2==0])



'''
some nice solutions in the forum:

1)

using the fact that the ratio of subsequent fibonacci terms approach the
golden ration at infinity or we can say that they are approximately equal
to the golden ratio phi = 1.618025751....

F(n+1) / F(n) = phi

fibonacci 1 1 2 3 5 8 13 21 34

EVERY THIRD TERM IS EVEN (Odd + Odd equals even)

so F(n+2) / F(n) = F(n+2) / F(n+1) * F(n+1) / F(n) = phi^2

or F(n+3) / F(n) = phi^3

so we start at 2 and multiply by phi^3 and rounding to the nerest integer.
'''

def evenFibPhi(n):
    phi = 1.618025751
    x = [2,]
    i = 0
    while x[-1] < n:
        x.append(int(round(x[i]*phi**3)))
        i += 1
    print x
    return sum(x[0:-2])

'''
i'm probably doing something wrong above however, the method is not mathy
at all because of the rounding


the solutions in the pdf indicate a method that can be used to avoid the
mod function. i.e. add every third number


'''

def evenFib2(n):
    '''this is not pythonic, can't be bothered to write it pythonically'''
    sum = 0
    a = 1
    b = 1
    c = a + b
    while a < n:
        sum += c
        a = b + c
        b = c + a
        c = a + b
    return sum
