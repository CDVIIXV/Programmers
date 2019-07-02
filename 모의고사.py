def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):     # q는 answers의 인덱스, a는 answers의 값
        for i, v in enumerate(p):       # i는 p의 인덱스, v는 p의 값
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


if __name__ == "__main__":
    print(solution([1,3,2,4,2]))
