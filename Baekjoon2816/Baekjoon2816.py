tv = []

def inp(tv):
    n = int(input())
    for _ in range(n):
        tv_name = input()
        tv.append(tv_name)

inp(tv)
res = ''
kbs1_n = tv.index('KBS1')
kbs2_n = tv.index('KBS2')

if kbs1_n < kbs2_n:
    res += '1' * kbs1_n
    res += '4' * kbs1_n
    res += '1' * kbs2_n
    res += '4' * (kbs2_n - 1)
else:
    res += '1' * kbs1_n
    res += '4' * kbs1_n
    res += '1' * (kbs2_n + 1)
    res += '4' * kbs2_n

print(res)