# l = [2, 5, 1, 3]

# f = lambda x:x**2



# result = any(map(lambda x: x%2==0, l))

# print (result)
# result = all(map(lambda x: x % 2 ==0 , l))

# print (result)

lista = []

def primes(tal):
    for b in range (1, tal):
        lista.append(b)
    for c in lista:
        if tal%c==0:
            tal2=tal/c
            print

primes(10)

