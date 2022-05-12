def numOfSeqK(k):
    seq = [i for i in map(int, input().split())]
    count_k = [[0 for y in range(len(seq))] for x in range(k)] # [i][j] é o número de subseqs de tamanho i - 1 terminando em j
    
    for i in range(len(seq)):
        count_k[0][i] = 1
 
    for l in range(1, k):
        for i in range(l, len(seq)):
            count_k[l][i] = 0
            for j in range(l - 1, i):
                if (seq[j] < seq[i]):
                    count_k[l][i] += count_k[l - 1][j]

    total = 0
    for j in range(k - 1, len(seq)):
        total += count_k[k - 1][j]
    print(total)


n, k = map(int, input().split())
while n != 0:
    numOfSeqK(k)
    n, k = map(int, input().split())