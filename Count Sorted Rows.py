#Count Sorted Rows
row=int(input())
col=int(input())
a=[[int(input("Enter the value:")) for i in range(row)]for j in range(col)]
def cou_mat(mat):
    c=0
    for i in mat:
        x=sorted(i)
        
        if i!=x:
            c=c+1
            print(c)
ans=cou_mat(a)
