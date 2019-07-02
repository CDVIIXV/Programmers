def convert(number, radix):
    letter = '0123456789ABCDEF'
    q, r = divmod(number, radix)
    if q == 0:
        return letter[r]
    else:
        return convert(q, radix) + letter[r]


def solution(n, t, m, p):
    digits = []
    count = 0
    while len(digits) < (t-1) * m + p:
        digits += convert(count, n)
        count += 1
    return ''.join(digits[p-1::m][:t])


if __name__ == "__main__":
    print(solution(16, 16, 2, 1))
