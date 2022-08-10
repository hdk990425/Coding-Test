def inp(N, k):          # 입력 함수
    for _ in range(N):
        inp_k, inp_gold, inp_silver, inp_bronze = map(int, input().split())
        if inp_k > N:
            break
        country.append(inp_k)
        gold.append(inp_gold)
        silver.append(inp_silver)
        bronze.append(inp_bronze)


country = []
gold = []
silver = []
bronze = []
want = []
rank = 1

N, k = map(int, input().split())
inp(N, k)

wi = country.index(k)       # 순위를 구하고 싶은 나라의 index
want.append(country[wi])    # want array에 나라이름, 금, 은, 동 개수 넣어준다.
want.extend([gold[wi], silver[wi], bronze[wi]])

for i in range(N):
    if want[1] == gold[i]:          # i번째 값과 want의 gold 같으면 silver 비교
        if want[2] == silver[i]:    # silver 같으면 bronze 비교
            if want[3] < bronze[i]: # gold, silver 같은데 bronze 작으면 i번째 값보다 순위 낮으므로 +1
                rank += 1
        elif want[2] < silver[i]:   # gold 같은데 silver 작아도 순위 낮으므로 +1
            rank += 1
    elif want[1] < gold[i]:         # gold 작아도 순위 낮으므로 +1
        rank += 1

print(rank)                 # 결과 출력