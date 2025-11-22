answer = 0

def dfs(current_fatigue, count, dungeons, visited):
    global answer
    answer = max(answer, count)

    for i in range(len(dungeons)):
        req, cost = dungeons[i]

        if not visited[i] and current_fatigue >= req:
            visited[i] = True
            dfs(current_fatigue - cost, count + 1, dungeons, visited)
            visited[i] = False  # 백트래킹


def solution(k, dungeons):
    visited = [False] * len(dungeons)

    dfs(k, 0, dungeons, visited)
    return answer
