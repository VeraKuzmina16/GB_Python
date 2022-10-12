import random
a = [random.randint(1,10) for x in range (10)]
print(a)
x = [a[i] for i in range(1, len(a), 2)]
print(x)
print(sum(x))
