#Maximum path sum in matrix
row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
a=[[int(input("Enter the value: ")) for i in range(row)] for j in range(col)]
def ma(mat):
    a=[]
    for i in mat:
        a.append(max(i))
    print(sum(a))
ans=ma(a)