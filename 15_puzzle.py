n = 4
l = []

def print_matrix(l, n):
    print()
    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()

for i in range(n):
    tl = []
    for j in range(n):
        ip = int(input())
        tl.append(ip)
    l.append(tl)

print_matrix(l, n)

for i1 in range(n):
    for j1 in range(n):
        ii = i1
        jj = j1

        si = i1
        sj = j1+1
        if j1+1 == n:
            si = i1+1
            sj = 0
            if si == n+1:
                break

        for i2 in range(si, n):
            for j2 in range(sj, n):
                if l[i2][j2] < l[ii][jj]:
                    ii = i2
                    jj = j2
        
        temp = l[i1][j1]
        l[i1][j1] = l[ii][jj]
        l[ii][jj] = temp

print_matrix(l, n)

"""
9
4
1
12
5
3
10
6
2
15
13
7
14
8
16
11
"""
