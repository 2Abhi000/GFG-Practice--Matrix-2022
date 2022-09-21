#Sum of elements in a matrix
row=int(input())
col=int(input())
a=[[int(input("Enter the value:")) for i in range(row)]for j in range(col)]
def sum_mat(mat):
    a=[]
    for i in mat:
        a.append(sum(i))
    print(sum(a))
ans=sum_mat(a)
