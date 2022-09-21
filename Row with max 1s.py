#Row with max 1s
row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
a=[[int(input("Enter the value: ")) for i in range(row)] for j in range(col)]
def matc(mat):
    d={}
    for i in range(len(mat)):
        c=0
        for j in range(len(mat)):
            if mat[i][j]==1:
                c=c+1
        d[c]=i
    
    if len(d)==1:
        print(0)
        return
    max_row=max(d)
    print(d[max_row])
                
ans=matc(a)