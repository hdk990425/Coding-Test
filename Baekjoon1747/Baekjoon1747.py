import math

N = int(input())

for i in range(N, 10000000):
    if i == 1:
        continue
    s = 0
    i_str = str(i)
    if i_str == i_str[::-1]:
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                s = s + 1
    if s == 1:
        print(i_str)
        break
