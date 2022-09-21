#Count zeros in a sorted matrix
row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
a=[[int(input("Enter the value: ")) for i in range(row)] for j in range(col)]
def matc(mat):
    a=[]
    for i in mat:
        a.append(i.count(0))
    print(sum(a))
                
ans=matc(a)
