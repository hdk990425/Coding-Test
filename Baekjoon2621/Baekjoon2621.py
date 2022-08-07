n = 5
c_color = []
c_num = []
max = 0             # 최대 점수
t_max = 0
color_n = {'R':0, 'G':0, 'B':0, 'Y':0}
num_n = [0 for _ in range(0, 10)]

for _ in range(n):
    inp_color, inp_num = input().split()
    c_color.append(inp_color)
    c_num.append(int(inp_num))

# 같은 색상, 숫자 개수
for i in range(n):
    color_n[c_color[i]] += 1
    num_n[c_num[i]] += 1


sort_num = c_num
sort_num.sort()
# 1
if 5 in color_n.values() and sort_num[0]+1 == sort_num[1] and sort_num[1]+1 == sort_num[2] and sort_num[2]+1 == sort_num[3] and sort_num[3]+1 == sort_num[4]:
    max = 900 + sort_num[4]

# 2
elif 4 in num_n:
    max = 800 + num_n.index(4)


# 3
elif 3 in num_n and 2 in num_n:
    max = 10*num_n.index(3) + num_n.index(2) + 700


# 4
elif 5 in color_n.values():
    for i in range(9, 0, -1):
        if num_n[i] >= 1:
            max = 600 + i
            break


# 5
elif sort_num[0]+1 == sort_num[1] and sort_num[1]+1 == sort_num[2] and sort_num[2]+1 == sort_num[3] and sort_num[3]+1 == sort_num[4]:
    max = 500 + sort_num[4]

# 6
elif 3 in num_n:
    max = num_n.index(3) + 400

# 7, 8
elif 2 in num_n:
    num1 = num_n.index(2)
    copy_num_n = num_n
    copy_num_n[num1] = 0
    if 2 in copy_num_n:     # 7
        num2 = copy_num_n.index(2)
        if num1 >= num2:
            max = 300 + num1*10 + num2
        else:
            max = 300 + num2*10 + num1
    else:                   # 8
        max = 200 + num1

# 9
else:
    max = sort_num[4] + 100

print(max)