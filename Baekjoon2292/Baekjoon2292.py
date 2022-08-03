# 밑의 for문의 경우도 돌아가지만 baekjoon에서 시간초과 뜸
# N = int(input())
#
# for i in range(1, (N//6)+2):
#     if (N-1 > 3*i*(i-1)) & (N-1 <= 3*(i+1)*i):
#         print(i+1)

N = int(input())
i=0

while N-1 >= 3*i*(i-1):     # N이 1인 경우를 생각해서 등호를 넣어 줌
    if N-1 <= 3*(i+1)*i:
        print(i+1)
        break
    else:
        i = i+1