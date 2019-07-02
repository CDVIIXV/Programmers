def solution(n, costs):
    '''
    크루스칼 알고리즘
    :param n: 정점의 개수
    :param costs: [출발정점, 도착정점, 가중치] 리스트
    :return: 최소신장트리 총 가중치 비용 
    '''
    answer = 0
    costs.sort(key=lambda element:element[2])
    tree = [0] * n
    treeCount = 1
    for value in costs:
        v1 = value[0]
        v2 = value[1]
        cost = value[2]
        if tree[v1] == 0 and tree[v2] == 0: # 둘 다 속해짔지 않을 때,
            tree[v1] = tree[v2] = treeCount
            treeCount += 1
            answer += cost
        elif tree[v1] * tree[v2] == 0:      # 한 부분만 속해있을 때,
            maximum = tree[v1] if tree[v1] > tree[v2] else tree[v2]
            tree[v1] = tree[v2] = maximum
            answer += cost
        elif tree[v1] != tree[v2]:       # 둘이 다른 부분에 속해있을 때,
            minimum = tree[v1] if tree[v1] < tree[v2] else tree[v2]
            maximum = tree[v1] if tree[v1] > tree[v2] else tree[v2]
            for i, v in enumerate(tree):
                if v == maximum:
                    tree[i] = minimum
            answer += cost
        if tree.count(1) == n:
            break
    return answer


if __name__ == "__main__":
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
