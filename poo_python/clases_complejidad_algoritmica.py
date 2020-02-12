
def constante(n):
    return 1

def log(n):
    if n == 10:
        p = 1
    elif n == 100:
        p = 2 
    elif n == 1000:
        p = 3
    else:
        p = 10000000000000000000000
    return p

def exponente(n):
    ex = 2**n
    return ex
    
if __name__ == "__main__":
    n = 1000000
    print(exponente(n))
    