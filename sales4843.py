def parse(L):
    parsedlist = L[0:2]
    count = 2
    for i in range(parsedlist[0]):
        k = count
        size = parsedlist[-1]
        parsedlist.append([L[a] for a in range(k,k+size)])
        if i<parsedlist[0]-1:
            parsedlist.append(L[k+size])
        count += size+1
    return parsedlist

def sales(A):
    B = []
    for i in range(len(A)):
        B.append(len([x for x in A[:i] if x<= A[i]]))
    print(sum(B))

num_of_lists = int(input())
for i in range(num_of_lists):
    cur_arr = []
    arr_len = int(input())
    cur_arr = list(map(lambda x: int(x), input().split(' ')))
    sales(cur_arr)

# S = [2,5,38, 111, 102, 111, 177, 8, 276, 284, 103, 439, 452, 276, 452, 398]
# S = input()
# sales(S)

#2
#5
#38 111 102 111 177
#8
#276 284 103 439 452 276 452 398
