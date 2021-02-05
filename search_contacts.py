
A = ["adam", "eva", "leo"]
B = ["1212121", "111111111", "444555666"]
P = "112"


def solution(A,B,P):
    results = []
    count = 0
    result = 'NO CONTACT'
    for x in B:
        if x.find(P) >= 0:
            results.append(A[count])

        count = count + 1

    results = sorted(results)

    if results:
        result = results[0]
    return result


print(solution(A,B,P))