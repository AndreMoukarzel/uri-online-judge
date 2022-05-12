#include <iostream>
 
using namespace std;


int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
 
int min_blocks(int block_sizes[], int num_blocks, int size) {
    int min_bps[size + 1]; // min blocks per size
    int i, j;
    
    qsort(block_sizes, num_blocks, sizeof(int), compare);
    if(size % block_sizes[num_blocks - 1] == 0)
        return size / block_sizes[num_blocks - 1];
    
    for(i = 0; i <= size; i++)
        min_bps[i] = 999999;
    min_bps[0] = 0;
    for(i = 0; i < num_blocks; i++) {
        for(j = block_sizes[i]; j <= size; j++)
             min_bps[j] = min(min_bps[j], min_bps[j - block_sizes[i]] + 1);
    }
    
    return min_bps[size];
}


int main() {
    int block_sizes[26];
    int test_num, num_blocks, size, i, j;
    
    scanf("%d", &test_num);
    for(i = 0; i < test_num; i++) {
        scanf("%d %d", &num_blocks, &size);
        for (j = 0; j < num_blocks; j++)
            scanf("%d", &block_sizes[j]);
        printf("%d\n", min_blocks(block_sizes, num_blocks, size));
    }
    return 0;
}
