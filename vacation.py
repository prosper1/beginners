Y = 2021
A = 7
B = 9
W = 4


def solution(Y, A, B, W):
    # write your code in Python 3.6

    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    first_mondays = [W]
    last_sunday = []
    first_monday = W

    for x in range(1,B):

        
        last_monday = first_monday + 28
        print(last_monday)
        if last_monday < month[x]:
            first_monday = (last_monday + 7) - month[x]

        else:
            first_monday = last_monday - month[x]


        first_mondays.append(first_monday)

    
    
    sunday = (first_mondays[B-1] + 6) + 21
    
    if sunday >= month[B]:
        last_sunday = sunday - 7

    else:
        last_sunday = sunday

    
    return [first_mondays[A-1],last_sunday]


print(solution(Y,A,B,W))