def solution(S):
    s_cleaned = S.replace("-","").replace(" ","")
    results = ''
    print(s_cleaned)
    count = len(s_cleaned)

    for x in range(0,count):

        if x%3 == 0:
            results = results + s_cleaned[x:x+3] + '-'

    
    return results[0:-1]


print(solution('00-44 48 5555 8361'))