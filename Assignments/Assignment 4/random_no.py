import random
j = 0
a = [0]*64
while j < 100000:
    for i in range(64):
        rand = (random.randint(0,32767))%2
        rand += 48
        a[i] = rand
    for i in range(64):
        print(chr(a[i]),end='')
    print()
    j += 1