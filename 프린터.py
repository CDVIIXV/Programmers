def solution(priorities, location):
    answer = 0
    while len(priorities):
        pivot = priorities[0]
        for i in priorities[1:]:
            if i > pivot:
                priorities.pop(0)
                priorities.append(pivot)
                break
        else:
            answer += 1
            priorities.pop(0)
            if location == 0:
                break
        location = location - 1 if location > 0 else len(priorities) - 1
    return answer


if __name__ == "__main__":
    print(solution([1, 1, 9, 1, 1, 1], 0))
