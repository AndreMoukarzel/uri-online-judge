#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;


void dfsStack(int u, vector<vector<int>> neighbors, vector<int> visited, vector<int> stack) {
    visited[u] = 1;
 
    for (auto& v : neighbors[u]) {
        if (visited[v] == 0)
            dfs(v, neighbors, visited, stack);
    }
    stack.push_back(u);
}
 

void bottom(int n, int e) {
    int u, v, visited[n];
    vector<vector<int>> neighbors;
    vector<vector<int>> inv_neighbors;
    vector<int> stack;
    
    for (int i = 0; i < e; i++) {
        cin >> u >> v;
        neighbors[u - 1].push_back(v - 1);
        inv_neighbors[v - 1].push_back(u - 1);
    }
 
    memset(visited, 0, sizeof visited);
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0)
            dfsStack(i, neighbors, visited, stack);
    }

    // not completed...
 
    cout << *min_element(dist.begin(), dist.end());
}
 

int main() {
    int v, e;
    
    scanf("%d", &n);
    while (n != 0) {
        scanf("%d", &e);
        bottom(n, e);
    }
    return 0;
}