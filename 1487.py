# -*- coding: utf-8 -*-


def instancia(number, ride_num: int, total_time: int):
    durations = []
    scores = []
    for ride in range(ride_num):
        duration, score = map(int, input().split())
        durations.append(duration)
        scores.append(score)
    
    print("Instancia ", number)
    print(mochila_booleana_com_repeticao(durations, scores, ride_num, total_time), end="\n\n")


def mochila_booleana(w, v, n, W):
    t = [[0 for x in range(W + 1)] for y in range(n + 1)]
    
    for Y in range(1, W + 1):
        for i in range(1, n + 1):
            if w[i] > Y:
                t[i][Y] = t[i - 1][Y]
            else:
                t[i][Y] = max(t[i - 1][Y], t[i - 1][Y - w[i]] + v[i])
    return t[n][W]


def mochila_booleana_com_repeticao(w, v, n, W):
    t = [0 for i in range(W + 1)]
 
    for Y in range(W + 1):
        for i in range(n):
            if w[i] <= Y:
                t[Y] = max(t[Y], t[Y - w[i]] + v[i])
    return t[W]
    

ride_num, total_time = map(int, input().split())
i = 0
while ride_num != 0:
    instancia(i, ride_num, total_time)
    
    ride_num, total_time = map(int, input().split())
