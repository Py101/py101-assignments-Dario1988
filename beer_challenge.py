from functools import reduce

def fattoriale(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
    
