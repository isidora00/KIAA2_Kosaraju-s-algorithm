#include <iostream>
#include <vector>
#include <stack>
#include <set>

using namespace std;

class Graph
{
    int V;
    vector<int> *adj;
    Graph getTransposeGraph();
    void DFSReversedGraph(Graph &G, int v, vector<bool> &visited, stack<int> &visitOrder);
    void DFS(int v, vector<bool> &visited, vector<int> &currentComponent);

public:
    Graph(int V)
    {
        this->V = V;
        adj = new vector<int>[V];
    }
    ~Graph() { delete[] adj; };
    void addEdge(int v, int w);
    vector<vector<int>> findComponents();
    static void random_edge(int n, int &i, int &j);
    static Graph *generateRandomGraph(int n, int m);
    static void calcuateExecutionTime(string output, int leftBound, int rightBound);
};