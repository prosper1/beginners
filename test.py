

def solution(A):
    a_sorted = sorted(A)
    first_small_integer = 0
    count = 0
    print(a_sorted)
    
    for a in a_sorted:
        
        if count < len(a_sorted)-1:
            if a_sorted[count+1] - 1 != a_sorted[count] and  a_sorted[count+1] != a_sorted[count] :
                first_small_integer = a_sorted[count] + 1
                print(first_small_integer)
                return first_small_integer

        if a_sorted[count] == len(a_sorted)-1:
            return a_sorted[count] + 1



        count = count + 1 

A = [-1,-3]
B =[1,3,1,4,6,2]
C =[1,2,3]

print(solution(B))
print(solution(C)) 
solution(A) 

