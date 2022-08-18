def search(a, b):
    if ground[a][b] == 1:
        ground[a][b] = 0  # 지나간 땅은 0으로 체크
        if a < n - 1:  # a가 m-1과 같으면 a+1하면 안됨
            search(a + 1, b)  # 재귀를 활용하여 옆의 땅 체크
        if b < m - 1:  # 위와 같은 이유
            search(a, b + 1)
        if b > 0:
            search(a, b - 1)
        if a > 0:
            search(a - 1, b)
    elif ground[a][b] == 0:  # 재귀를 탈출하는 법
        return


test_case = int(input())
for _ in range(test_case):
    c = 0
    m, n, k = map(int, input().split())
    ground = [[0] * m for __ in range(n)]

    for ___ in range(k):  # 땅 위치 입력받는 부분
        inp_a, inp_b = map(int, input().split())
        ground[inp_b][inp_a] = 1

    for i in range(n):  # 연결되어 있지 않은 땅의 개수 찾는 부분
        for j in range(m):  # search 함수에서 지나온 부분은 0으로 체크하므로
            if ground[i][j] == 1:  # 1을 만나는 부분만 세면 됨
                c += 1
                search(i, j)

    print(c)
