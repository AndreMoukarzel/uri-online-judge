#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
vector<int> dist;
vector<int> color; // 0 = white, 1 = gray, 2 = black, 3 = cycle
 
void dfs(int u, vector<vector<int>> neighbors, int this_dist) {
    color[u] = 1;
 
    for (auto& node : neighbors[u]) {
        if (color[node] == 0)
            dfs(node, neighbors, this_dist + 1);
        else if (color[node] == 1) {
            color[u] = 3;
            dist[u] = -1;
        }
    }
    if (color[u] != 3) {
        color[u] = 2;
        dist[u] = max(dist[u], this_dist);
    }
}
 

void minDist(int n) {
    int m, v;
    vector<vector<int>> neighbors;
    dist.resize(n + 1, 0);
 
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &m);
        for (int j = 0; j < m; j++) {
            scanf("%d", &v);
            neighbors[i].push_back(v - 1);
        }
    }
 
    for (int i = 0; i < n; i++) {
        color.clear();
        color.resize(n + 1, 0);
        dfs(i, neighbors, 0);
    }
 
    cout << *min_element(dist.begin(), dist.end());
}
 

int main() {
    int n;
    
    while (cin >> n) {
        for (int i = 0; i < n; i++)
            minDist(n);
    }
    return 0;
}