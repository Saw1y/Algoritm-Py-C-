# Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.

# Входные данные
# Во входном файле записано два числа 𝑁
#  и 𝑀 (0 < 𝑁 ≤ 100000, 0 ≤ 𝑀 ≤ 100000). В следующих 𝑀 строках записаны по два числа 𝑖 и 𝑗(1 ≤ 𝑖, 𝑗≤ 𝑁), которые означают, что вершины 𝑖и 𝑗 соединены ребром.

# Выходные данные
# В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем формате: 
# в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.

import sys
sys.setrecursionlimit(200000)


n, m = map(int, input().split())

graph = {i + 1: set() for i in range(n)}
for _ in range(m):
    vertex, edge = map(int, input().split())
    graph[vertex].add(edge)
    graph[edge].add(vertex)


def dfs(start, component):
    visited[start] = True
    component.append(start)
    for v in graph[start]:
        if not visited[v]:
            dfs(v, component)


visited = [False] * (n + 1)
components = []

for i in range(1, n + 1):
    if not visited[i]:
        component = []
        dfs(i, component)
        components.append(component)

print(len(components))
for i in range(len(components)):
    print(len(components[i]))
    print(*components[i])
