n = input()
first_n = 0
i = 0

while first_n != n:
    if int(n) < 10 and len(n) == 1:         # len(n) == 1 조건을 넣어준 이유: 처음엔 상관없지만 뒤에서 n = n[1] + str(n_sum%10) 을 한 경우에 n이 05와 같이 나올 때가 있다.
        n = '0' + n                         # 이러한 경우 len조건이 없으면 n = 005가 되기 때문에 밑에 n_sum 하는 부분에서 0 + 0 이 돼서 n_sum이 0이 나오게 되므로 오류가 생긴다.
    if i == 0:
        first_n = n
    n_sum = int(n[0]) + int(n[1])
    n = n[1] + str(n_sum%10)
    i += 1

print(i)