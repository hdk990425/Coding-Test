def check_horizontal_space(array, num):
    h_sum = 0
    for i in range(num):
        h_check = 0
        for j in range(num):
            if array[i][j] == ".":
                h_check += 1
                if j + 1 == num:
                    if h_check >= 2:
                        h_sum += 1
                    h_check = 0
            elif array[i][j] == "X":
                if h_check >= 2:
                    h_sum += 1
                h_check = 0
    return h_sum


def check_vertical_space(array, num):
    v_sum = 0
    for i in range(num):
        v_check = 0
        for j in range(num):
            if array[j][i] == ".":
                v_check += 1
                if j + 1 == num:
                    if v_check >= 2:
                        v_sum += 1
                    v_check = 0
            elif array[j][i] == "X":
                if v_check >= 2:
                    v_sum += 1
                v_check = 0
    return v_sum


N = int(input())
room = [list(map(str, input())) for _ in range(N)]  # for문 돌리는 경우 변수명이 필요없을 땐 _ 써도 좋을 듯

print(check_horizontal_space(room, N), check_vertical_space(room, N))
