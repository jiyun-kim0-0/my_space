
#stack을 이용함
#깊이 우선 탐색 #DFS 메서드 정의
def dfs(graph,v,visited):
    
    #현재 노드 방문 처리
    visited[v] = True
    print(v,end=' ') #해당 노드를 방문했다는 의미로 노드 번호 출력 / 
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문함.
    for i in graph[v]: #그래프 리스트의 인덱스
        if not visited[i]: #인접된 노드가 방문 되지 않은 상태라면, 해당 노드에 대해서 재귀함수를 이용하여 방문
            dfs(graph,i,visited) #재귀함수
            


# 2차원 연결 리스트를 이용해 각 노드에 연결된 정보를 표현함.
graph = [
    [], #인덱스 0 는 비워둔다.
    [2,3,8], #1번 노드와 연결된 노드들을 표시함
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 1차원 리스트를 이용해 각 노드가 방문된 정보를 표현
visited = [False] * 9 # False로 정보 초기화 # 노드 1~8 (인덱스 0을 포함해서 * 9)

#정의된 함수 호출함
dfs(graph,1,visited) #방문한 노드를 순서대로 출력함.
    