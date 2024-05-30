import random

a = []
b = []
c = []

for i in range(0,20):
    num = random.randint(1,30)
    a.append(num)

for i in range(0,20):
    num = random.randint(1,30)
    b.append(num)

for num in a:
    if num in b:
        if num not in c:
            c.append(num)

print(f"list a: {a}")
print(f"list b: {b}")
print(f"list c: {c}")
