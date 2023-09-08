# NxM 얼음틀에 0은 구멍, 1은 칸막이 0끼리 붙을수 있음 => 전체 얼음덩어리 갯수 구하세용 

# N,M 공백으로 구분하여 입력받기 
n,m = map(int,input().split())

# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# dfs로 특정한 노드를 방문 한 뒤에 연결된 모든 노드들 방문 
def dfs(x,y):
    # 주어진 범위를 벗어나면 종료 
    if x <= -1 or x >=n or y<= -1 or y >=m :
        return False
    # 현재 노드 아직 방문 안했다면 
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 
        graph[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행 
        if dfs(i,j) == True:
            result+=1

print(result)