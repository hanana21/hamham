# DFS: 깊이 우선 탐색, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘 
# 그래프의 기본 구조: 노드, 간선, 인접하다(간선으로 연결되어있다면)
# 그래프의 2종류 : 
#     1) 인접 행렬: 2차원 배열에 각 노드가 연결된 형태를 기록 (연결안되면 무한, 자신은 0 나머지는 간선)
INF = 987654321
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
#      2)인접 리스트: 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장 
graph2 =[[] for _ in range(3)]
graph2[0].append((1,7))
graph2[0].append((2,5))
graph2[1].append((0,7))
graph2[2].append((0,5))