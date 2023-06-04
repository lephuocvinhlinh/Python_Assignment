
def solution(lst, n):
    result = [[] for _ in range(n)]
    for element in lst:
        result[element % n].append(element)
    return result

s = input()
lst = list(map(int, s.split()))
n = int(input())

print(solution(lst, n))
