h = 2
h1 = 19

print(h is not h1)
print(h1 % h)


m = 7
for i in range(1, 101):
    x = i % m
    print(f'{x} = {i} % {m}')