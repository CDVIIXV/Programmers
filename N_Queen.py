def backtracking(index, n):
    if index == n:
        return 1
    answer = 0
    left = n * index
    right = n * (index + 1)
    while left < right:
        for i in range(0, index):
            mod1 = left % n
            mod2 = position[i] % n
            if mod1 == mod2 or abs(mod1 - mod2) == index - i:
                break
        else:
            position[index] = left
            answer += backtracking(index + 1, n)
        left += 1
    return answer


def solution(n):
    global position
    position = [0 for i in range(0, n)]
    return backtracking(0, n)


if __name__ == "__main__":
    print("\n".join(str(solution(i)) for i in range(1, 9)))
