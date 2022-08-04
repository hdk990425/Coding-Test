x = int(input())
i = 1

while x > i:
    x = x - i
    i = i + 1

if i%2==0:      # i가 짝수번째 줄이면 큰 값이 뒤에 들어감
    print(f"{x}/{i+1-x}")
else:
    print(f"{i+1-x}/{x}")