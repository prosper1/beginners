Y = 2014
A = 7
B = 9
W = 'Wednesday'


def solution(Y, A, B, W):
    # write your code in Python 3.6

    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]


    first_monday = 0
    if W == 'Monday':
        first_monday = 1
        first_mondays = [1]
    else:
        first_mondays = [8-days.index(W)]
        first_monday = 8 - days.index(W)

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

    sum_days = first_mondays[A-1] + last_sunday
    for x in range(A+1,B):
        sum_days = sum_days + month[x]
    
    return sum_days / 7


    
print(solution(Y,A,B,W))