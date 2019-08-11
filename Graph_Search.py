import numpy as np
from Queue_As_Linked_List import LinkedQueue


class GraphSearch:
    def __init__(self, vertices):
        self.adjmatrix = np.zeros((vertices, vertices))
        self.vertices = vertices
        self.visited = [0] * self.vertices

    def DepthFirstSearch(self, source):
        i = source
        if self.visited[i] == 0:
            print(i, end='-')
            self.visited[i] = 1
        for j in range(self.vertices):
            if self.adjmatrix[i][j] != 0 and self.visited[j] == 0:
                self.DepthFirstSearch(j)

    def BreadthFirstSearch(self, source):
        self.visited = [0] * self.vertices
        i = source
        q = LinkedQueue()
        print(i, end='-')
        self.visited[i] = 1
        q.enqueue(i)
        while not q.is_empty():
            i = q.dequeue()
            for j in range(self.vertices):
                if self.adjmatrix[i][j] != 0 and self.visited[j] == 0:
                    print(j, end='-')
                    self.visited[j] = 1
                    q.enqueue(j)
        self.visited = [0] * self.vertices

    def insert_edge(self, v1, v2, weight=1):
        self.adjmatrix[v1][v2] = weight

    def delete_edge(self, v1, v2):
        self.adjmatrix[v1][v2] = 0

    def get_edge(self, v1, v2):
        return self.adjmatrix[v1, v2]

    def vcount(self):
        return self.vertices

    def ecount(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if not self.adjmatrix[i][j] == 0:
                    count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self.vertices):
            if not self.adjmatrix[i][v] == 0:
                count += 1
        return count

    def outdegree(self, v):
        count = 0
        for i in range(self.vertices):
            if not self.adjmatrix[v][i] == 0:
                count += 1
        return count

    def display(self):
        print(self.adjmatrix)


G = GraphSearch(8)
G.insert_edge(0,2)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(4,2)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(2,7)
G.insert_edge(2,4)
G.insert_edge(3,7)
G.insert_edge(3,1)
G.insert_edge(4,5)
G.insert_edge(5,3)
G.insert_edge(6,1)
G.insert_edge(6,4)
G.insert_edge(7,2)

print('Graph Matrix')
G.display()

print('No. of vertices: ', G.vcount())
print('No. of edges: ', G.ecount())
print('No. of outdegrees on vertex 3: ', G.outdegree(3))

print('\nBreadth first search:')
G.BreadthFirstSearch(0)

print('\nDepth first search:')
G.DepthFirstSearch(0)

