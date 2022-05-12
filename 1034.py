def min_blocks(block_sizes, num_blocks, size):
    if size % block_sizes[-1] == 0:
        return int(size/block_sizes[-1])
    
    min_bps = [9999999 for _ in range(size + 1)]
    min_bps[0] = 0 # min blocks per size
    for i in range(num_blocks):
        for j in range(block_sizes[i], size + 1):
            min_bps[j] = min(min_bps[j], min_bps[j - block_sizes[i]] + 1)
    return min_bps[size]

for test_num in range(int(input())):
    num_blocks, size = map(int, input().split())
    block_sizes = [b for b in map(int, input().split())]
    print(min_blocks(block_sizes, num_blocks, size))