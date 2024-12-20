# Невзвешенный ориентированный граф задан своей матрицей смежности. Требуется построить его транзитивное замыкание, то есть матрицу, в которой в 𝑖
# -й строке и 𝑗-м столбце находится 1, если от вершины 𝑖можно добраться до вершины 𝑗, и 0 - иначе.

# Входные данные
# В первой строке дано число 𝑁
#  (1≤𝑁≤100) - число вершин в графе. Далее задана матрица смежности графа: в 𝑁
#  строках даны по 𝑁чисел 0 или 1 в каждой. -е число в -й строке всегда равно 1.

# Выходные данные
# Необходимо вывести матрицу транзитивного замыкания графа в формате, аналогичным формату матрицы смежности.

def floyd(graph, n):
    dist = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


n = int(input())
graph = [[0] * n for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = line[j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = -1

result = floyd(graph, n)
for i in range(n):
    for j in range(n):
        if result[i][j] != float("inf"):
            result[i][j] = 1
        else:
            result[i][j] = 0
for line in result:
    print(*line)
